from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import json
from datetime import datetime
from app.models.classifier import symptom_classifier

router = APIRouter()

# Request/Response models
class SymptomInput(BaseModel):
    symptoms: str
    severity: int = 5  # 1-10 scale
    duration: str = "recent"  # recent, days, weeks, months
    user_id: str = "anonymous"

class ConditionPrediction(BaseModel):
    condition: str
    probability: float
    description: str
    urgency: str
    recommendations: List[str]

class SymptomResponse(BaseModel):
    predictions: List[ConditionPrediction]
    urgency: str  # emergency, urgent, routine
    recommendations: List[str]
    timestamp: str
    model_status: str

# Temporary data storage (will replace with database later)
user_history = {}

@router.post("/analyze-symptoms", response_model=SymptomResponse)
async def analyze_symptoms(input_data: SymptomInput):
    """
    Analyze user symptoms and return predictions using trained ML model
    """
    try:
        # Check if model is loaded
        if not symptom_classifier.is_trained:
            # Try to load saved model
            if not symptom_classifier.load_model():
                raise HTTPException(
                    status_code=503, 
                    detail="Model not trained. Please train the model first using train_model.py"
                )
        
        # Get predictions from ML model
        ml_predictions = symptom_classifier.predict(input_data.symptoms, top_k=3)
        
        if not ml_predictions:
            # Fallback if no predictions
            predictions = [
                ConditionPrediction(
                    condition="Unknown",
                    probability=0.1,
                    description="Unable to determine condition from symptoms",
                    urgency="routine",
                    recommendations=["Consult with a healthcare provider for proper diagnosis"]
                )
            ]
            urgency = "routine"
        else:
            # Convert ML predictions to response format
            predictions = [
                ConditionPrediction(
                    condition=pred['condition'],
                    probability=pred['probability'],
                    description=pred['description'],
                    urgency=pred['urgency'],
                    recommendations=pred['recommendations']
                )
                for pred in ml_predictions
            ]
            
            # Determine overall urgency (highest urgency from predictions)
            urgency_levels = {'routine': 0, 'urgent': 1, 'emergency': 2}
            max_urgency = max(pred['urgency'] for pred in ml_predictions)
            urgency = max_urgency
        
        # Get overall recommendations
        all_recommendations = []
        for pred in ml_predictions:
            all_recommendations.extend(pred['recommendations'])
        
        # Remove duplicates and limit to top 3
        recommendations = list(dict.fromkeys(all_recommendations))[:3]
        
        if not recommendations:
            recommendations = [
                "Monitor symptoms closely",
                "Stay hydrated and get adequate rest",
                "Consult a healthcare provider if symptoms persist or worsen"
            ]
        
        # Store in user history
        if input_data.user_id not in user_history:
            user_history[input_data.user_id] = []
        
        user_history[input_data.user_id].append({
            "symptoms": input_data.symptoms,
            "severity": input_data.severity,
            "timestamp": datetime.now().isoformat(),
            "predictions": [p.dict() for p in predictions]
        })
        
        return SymptomResponse(
            predictions=predictions,
            urgency=urgency,
            recommendations=recommendations,
            timestamp=datetime.now().isoformat(),
            model_status="active"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing symptoms: {str(e)}")

@router.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@router.get("/user-history/{user_id}")
async def get_user_history(user_id: str):
    """
    Get user's symptom history
    """
    history = user_history.get(user_id, [])
    return {
        "user_id": user_id,
        "entries": history,
        "total_entries": len(history)
    }