from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.services.auth_service import get_current_user
from app.database import get_database
from app.services.ai_mentor import ai_mentor_service
from app.services.daily_experience import daily_experience_service
from app.services.scaffold_engine import scaffold_engine

router = APIRouter(prefix="/api/ai", tags=["AI Mentor & Personalization"])

class PersonalizedTaskRequest(BaseModel):
    subject: str = "Mathematics"
    difficulty: int = 1
    base_objective: str = "Solve basic calculation"

class HintRequest(BaseModel):
    question: str
    correct_answer: str
    attempt_count: int = 1

class ScaffoldRequest(BaseModel):
    task: Optional[Dict[str, Any]] = None
    task_id: Optional[str] = None
    session_id: Optional[str] = None
    attempt_count: int = 1
    failed_attempts: Optional[int] = None
    hint_level: Optional[int] = None
    requested_level: Optional[int] = None

@router.post("/personalized-task")
async def generate_personalized_task(
    req: PersonalizedTaskRequest,
    current_user: dict = Depends(get_current_user)
):
    db = get_database()
    learner_id = current_user.get("learner_id")
    profile = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}
    state_doc = await db["learner_profile_state"].find_one({"learner_id": learner_id}) or {}

    learner_context = {
        "interests": profile.get("interests", ["space"]),
        "preferredLearningMode": profile.get("preferred_learning_modes", ["visual"])[0] if profile.get("preferred_learning_modes") else "visual",
        "currentState": state_doc.get("current_state", "FOCUSED"),
        "preferredTaskLength": profile.get("interaction_preferences", {}).get("task_size", "small"),
        "difficulty": req.difficulty,
        "recentPerformance": {"accuracy": 0.8}
    }

    personalized_task = await ai_mentor_service.generate_personalized_mission_task(
        subject=req.subject,
        learner_context=learner_context,
        base_objective=req.base_objective,
        difficulty=req.difficulty
    )

    return personalized_task

@router.post("/hint")
async def get_ai_hint(
    req: HintRequest,
    current_user: dict = Depends(get_current_user)
):
    db = get_database()
    learner_id = current_user.get("learner_id")
    profile = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}
    
    learner_context = {
        "interests": profile.get("interests", ["space"]),
        "preferredLearningMode": "visual"
    }

    hint_text = await ai_mentor_service.generate_gentle_hint(
        question=req.question,
        correct_answer=req.correct_answer,
        learner_context=learner_context,
        attempt_count=req.attempt_count
    )

    return {"hint": hint_text}

@router.post("/scaffold")
async def get_failure_scaffold(
    req: ScaffoldRequest,
    current_user: dict = Depends(get_current_user)
):
    db = get_database()
    learner_id = current_user.get("learner_id")
    profile = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}

    learner_context = {
        "interests": profile.get("interests", ["space"]),
        "preferredLearningMode": "visual"
    }

    task_obj = req.task
    if not task_obj and req.task_id:
        task_doc = await db["tasks"].find_one({"$or": [{"_id": req.task_id}, {"id": req.task_id}]})
        if task_doc:
            task_obj = task_doc
        else:
            task_obj = {
                "id": req.task_id,
                "question": "Photosynthesis & Plant Nutrition",
                "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
                "correct_answer": "Oxygen"
            }
    if not task_obj:
        task_obj = {
            "question": "What gas do green plants release during photosynthesis?",
            "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
            "correct_answer": "Oxygen"
        }

    attempts = req.attempt_count if req.attempt_count > 1 else (req.failed_attempts or req.attempt_count)
    target_level = req.requested_level or req.hint_level

    scaffold_result = await scaffold_engine.get_scaffold_response(
        task=task_obj,
        attempt_count=attempts,
        learner_context=learner_context,
        requested_level=target_level
    )

    return scaffold_result

@router.get("/daily-welcome")
async def get_daily_welcome(current_user: dict = Depends(get_current_user)):
    db = get_database()
    learner_id = current_user.get("learner_id")
    profile = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}
    
    # Get last session & progress
    last_session = await db["learner_sessions"].find_one({"learner_id": learner_id}, sort=[("started_at", -1)])
    progress = await db["progress"].find_one({"learner_id": learner_id})

    daily_exp = await daily_experience_service.construct_daily_experience(
        learner_profile=profile,
        previous_session=last_session,
        recent_progress=progress
    )

    return daily_exp
