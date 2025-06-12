import pandas as pd
import re
import string
from typing import List, Tuple
import pickle
import os

class DataProcessor:
    def __init__(self):
        self.stop_words = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
                              'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 
                              'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 
                              'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
                              'what', 'which', 'who', 'whom', 'this', 'that', 'these', 
                              'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 
                              'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 
                              'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 
                              'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
                              'through', 'during', 'before', 'after', 'above', 'below', 
                              'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under'])
    
    def load_dataset(self, file_path: str) -> pd.DataFrame:
        """
        Load dataset from Excel file
        """
        try:
            # Try reading as Excel first
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                df = pd.read_excel(file_path)
            else:
                df = pd.read_csv(file_path)
            
            print("Dataset loaded successfully!")
            print(f"Shape: {df.shape}")
            print(f"Columns: {df.columns.tolist()}")
            print(f"Unique conditions: {df['label'].nunique()}")
            
            return df
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return None
    
    def clean_text(self, text: str) -> str:
        """
        Clean and preprocess text
        """
        if not isinstance(text, str):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove stop words
        words = text.split()
        words = [word for word in words if word not in self.stop_words and len(word) > 2]
        
        return ' '.join(words)
    
    def prepare_training_data(self, df: pd.DataFrame) -> Tuple[List[str], List[str]]:
        """
        Prepare data for training
        """
        # Clean the text data
        df['cleaned_text'] = df['text'].apply(self.clean_text)
        
        # Filter out empty texts
        df = df[df['cleaned_text'].str.len() > 0]
        
        print(f"After cleaning: {len(df)} samples")
        print(f"Sample cleaned text: {df['cleaned_text'].iloc[0]}")
        
        return df['cleaned_text'].tolist(), df['label'].tolist()
    
    def get_condition_info(self, df: pd.DataFrame) -> dict:
        """
        Create condition information dictionary
        """
        condition_info = {}
        
        for condition in df['label'].unique():
            condition_samples = df[df['label'] == condition]
            
            # Basic info about each condition
            condition_info[condition] = {
                'name': condition,
                'sample_count': len(condition_samples),
                'description': f"Medical condition: {condition}",
                'urgency': self._determine_urgency(condition),
                'recommendations': self._get_recommendations(condition)
            }
        
        return condition_info
    
    def _determine_urgency(self, condition: str) -> str:
        """
        Determine urgency level based on condition name
        """
        condition_lower = condition.lower()
        
        # Emergency conditions
        emergency_conditions = ['heart attack', 'stroke', 'anaphylaxis', 'sepsis', 
                              'pneumonia', 'meningitis', 'appendicitis']
        
        # Urgent conditions  
        urgent_conditions = ['diabetes', 'hypertension', 'pneumonia', 'bronchitis',
                           'kidney', 'liver', 'infection']
        
        if any(emergency in condition_lower for emergency in emergency_conditions):
            return 'emergency'
        elif any(urgent in condition_lower for urgent in urgent_conditions):
            return 'urgent'
        else:
            return 'routine'
    
    def _get_recommendations(self, condition: str) -> List[str]:
        """
        Get recommendations based on condition
        """
        condition_lower = condition.lower()
        
        if 'psoriasis' in condition_lower:
            return [
                "Consult a dermatologist for proper diagnosis",
                "Avoid triggers like stress and certain medications",
                "Use moisturizers to keep skin hydrated",
                "Consider topical treatments as prescribed"
            ]
        elif 'diabetes' in condition_lower:
            return [
                "Monitor blood sugar levels regularly",
                "Follow prescribed medication schedule",
                "Maintain a balanced diet",
                "Schedule regular check-ups with your doctor"
            ]
        elif 'hypertension' in condition_lower:
            return [
                "Monitor blood pressure regularly",
                "Reduce sodium intake",
                "Exercise regularly as approved by doctor",
                "Take prescribed medications consistently"
            ]
        else:
            return [
                "Consult with a healthcare provider",
                "Monitor symptoms closely",
                "Follow prescribed treatment plan",
                "Seek immediate care if symptoms worsen"
            ]

# Create global instance
data_processor = DataProcessor()