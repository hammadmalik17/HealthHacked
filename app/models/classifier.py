from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle
import numpy as np
from typing import List, Dict, Tuple
import os
from app.services.data_processor import data_processor

class SymptomClassifier:
    def __init__(self):
        self.pipeline = None
        self.condition_info = {}
        self.is_trained = False
        self.model_path = "models/symptom_classifier.pkl"
        self.info_path = "models/condition_info.pkl"
    
    def train(self, dataset_path: str):
        """
        Train the classifier on the dataset
        """
        print("Loading and processing dataset...")
        
        # Load dataset
        df = data_processor.load_dataset(dataset_path)
        if df is None:
            raise Exception("Failed to load dataset")
        
        # Prepare training data
        texts, labels = data_processor.prepare_training_data(df)
        
        print(f"Training on {len(texts)} samples...")
        print(f"Unique conditions: {len(set(labels))}")
        
        # Create condition info
        self.condition_info = data_processor.get_condition_info(df)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            texts, labels, test_size=0.2, random_state=42, stratify=labels
        )
        
        # Create pipeline
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=5000,
                stop_words='english',
                ngram_range=(1, 2),  # Use both single words and pairs
                min_df=2,  # Ignore terms that appear in less than 2 documents
                max_df=0.95  # Ignore terms that appear in more than 95% of documents
            )),
            ('classifier', MultinomialNB(alpha=0.1))
        ])
        
        # Train the model
        print("Training classifier...")
        self.pipeline.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print("Training completed!")
        print(f"Accuracy: {accuracy:.3f}")
        print(f"Test samples: {len(X_test)}")
        
        self.is_trained = True
        
        # Save model
        self.save_model()
        
        return accuracy
    
    def predict(self, symptom_text: str, top_k: int = 3) -> List[Dict]:
        """
        Predict conditions for given symptom text
        """
        if not self.is_trained and not self.load_model():
            raise Exception("Model not trained and no saved model found")
        
        # Clean the input text
        cleaned_text = data_processor.clean_text(symptom_text)
        
        if not cleaned_text:
            return []
        
        # Get predictions with probabilities
        probabilities = self.pipeline.predict_proba([cleaned_text])[0]
        classes = self.pipeline.classes_
        
        # Get top predictions
        top_indices = np.argsort(probabilities)[-top_k:][::-1]
        
        predictions = []
        for idx in top_indices:
            condition = classes[idx]
            probability = probabilities[idx]
            
            # Only include predictions with reasonable probability
            if probability > 0.01:  # 1% threshold
                condition_data = self.condition_info.get(condition, {})
                
                predictions.append({
                    'condition': condition,
                    'probability': float(probability),
                    'description': condition_data.get('description', f"Medical condition: {condition}"),
                    'urgency': condition_data.get('urgency', 'routine'),
                    'recommendations': condition_data.get('recommendations', [
                        "Consult with a healthcare provider",
                        "Monitor symptoms closely"
                    ])
                })
        
        return predictions
    
    def save_model(self):
        """
        Save trained model and condition info
        """
        # Create models directory if it doesn't exist
        os.makedirs('models', exist_ok=True)
        
        # Save pipeline
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.pipeline, f)
        
        # Save condition info
        with open(self.info_path, 'wb') as f:
            pickle.dump(self.condition_info, f)
        
        print(f"Model saved to {self.model_path}")
    
    def load_model(self) -> bool:
        """
        Load saved model
        """
        try:
            if os.path.exists(self.model_path) and os.path.exists(self.info_path):
                # Load pipeline
                with open(self.model_path, 'rb') as f:
                    self.pipeline = pickle.load(f)
                
                # Load condition info
                with open(self.info_path, 'rb') as f:
                    self.condition_info = pickle.load(f)
                
                self.is_trained = True
                print("Model loaded successfully!")
                return True
            else:
                print("No saved model found")
                return False
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def get_model_info(self) -> Dict:
        """
        Get information about the trained model
        """
        if not self.is_trained:
            return {"status": "not_trained"}
        
        return {
            "status": "trained",
            "total_conditions": len(self.condition_info),
            "conditions": list(self.condition_info.keys()),
            "model_type": "TF-IDF + Naive Bayes"
        }

# Create global instance
symptom_classifier = SymptomClassifier()