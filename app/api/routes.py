from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import json
from datetime import datetime

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

class SymptomResponse(BaseModel):
    predictions: List[ConditionPrediction]
    urgency: str  # emergency, urgent, routine
    recommendations: List[str]
    timestamp: str

# Temporary data storage (will replace with database later)
user_history = {}

@router.post("/analyze-symptoms", response_model=SymptomResponse)
async def analyze_symptoms(input_data: SymptomInput):
    """
    Analyze user symptoms and return predictions
    """
    try:
        # For now, return mock data - we'll implement real ML later
        mock_predictions = [
            ConditionPrediction(
                condition="Common Cold",
                probability=0.6,
                description="Viral infection of upper respiratory tract"
            ),
            ConditionPrediction(
                condition="Seasonal Allergies",
                probability=0.3,
                description="Allergic reaction to environmental triggers"
            )
        ]
        
        # Simple urgency logic (we'll improve this)
        urgency = "routine"
        if "chest pain" in input_data.symptoms.lower():
            urgency = "urgent"
        if "can't breathe" in input_data.symptoms.lower():
            urgency = "emergency"
        
        recommendations = [
            "Monitor symptoms for 24-48 hours",
            "Stay hydrated and get adequate rest",
            "Consult a healthcare provider if symptoms worsen"
        ]
        
        # Store in user history
        if input_data.user_id not in user_history:
            user_history[input_data.user_id] = []
        
        user_history[input_data.user_id].append({
            "symptoms": input_data.symptoms,
            "severity": input_data.severity,
            "timestamp": datetime.now().isoformat(),
            "predictions": [p.dict() for p in mock_predictions]
        })
        
        return SymptomResponse(
            predictions=mock_predictions,
            urgency=urgency,
            recommendations=recommendations,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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