#!/usr/bin/env python3
"""
Training script for the symptom classifier
"""

import os
import sys
from app.models.classifier import symptom_classifier

def main():
    print("=== AI Symptom Checker - Model Training ===")
    
    # Check if dataset file exists
    dataset_path = input("Enter path to your dataset file (e.g., 'data/Symptom2Disease.xlsx'): ").strip()
    
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset file '{dataset_path}' not found!")
        print("Please make sure the file exists and try again.")
        return
    
    try:
        print(f"\nStarting training with dataset: {dataset_path}")
        print("This may take a few minutes...")
        
        # Train the model
        accuracy = symptom_classifier.train(dataset_path)
        
        print("\n✅ Training completed successfully!")
        print("📊 Model accuracy: {accuracy:.1%}")
        print("💾 Model saved to: models/symptom_classifier.pkl")
        
        # Test the model
        print("\n🧪 Testing the model...")
        test_symptoms = [
            "I have a headache and feel dizzy",
            "My skin is red and itchy with scaly patches",
            "I have chest pain and shortness of breath"
        ]
        
        for symptom in test_symptoms:
            print(f"\nTest: '{symptom}'")
            predictions = symptom_classifier.predict(symptom, top_k=2)
            
            if predictions:
                for pred in predictions:
                    print(f"  - {pred['condition']}: {pred['probability']:.1%} ({pred['urgency']})")
            else:
                print("  - No predictions found")
        
        print("\n🎉 Model is ready to use!")
        print("You can now start the API server with: python run.py")
        
    except Exception as e:
        print(f"\n❌ Training failed: {e}")
        print("Please check your dataset format and try again.")

if __name__ == "__main__":
    main()