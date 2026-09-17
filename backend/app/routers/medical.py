from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from datetime import datetime
from app.database import get_database
from app.models.medical import MedicalQuestion, MedicalProfileSubmit
from app.services.auth_service import get_current_user
from app.services.medical_service import get_medical_questions

router = APIRouter(prefix="/api/medical", tags=["Medical"])

@router.get("/questions/{learner_id}", response_model=List[MedicalQuestion])
async def fetch_questions(learner_id: str, current_user: dict = Depends(get_current_user)):
    db = get_database()
    learner = await db["learners"].find_one({"_id": learner_id} if len(learner_id) != 24 else {"_id": __import__("bson").ObjectId(learner_id)})
    
    # If not found by ID, maybe it's passed directly as a condition string for the initial fetch?
    # Actually, the user profile has the learner ID. Let's get the condition.
    condition = "ADHD"
    if learner and "condition" in learner:
        condition = learner["condition"]
        
    return get_medical_questions(condition)

@router.post("/submit")
async def submit_medical_profile(profile: MedicalProfileSubmit, current_user: dict = Depends(get_current_user)):
    db = get_database()
    
    doc = {
        "learner_id": profile.learner_id,
        "caregiver_id": current_user["id"],
        "condition": profile.condition,
        "answers": [answer.dict() for answer in profile.answers],
        "submitted_at": datetime.utcnow()
    }
    
    await db["medical_profiles"].insert_one(doc)
    
    # Update learner document if needed
    # (Optional: we already set condition in registration)
    
    return {"status": "success", "message": "Medical profile saved successfully"}
