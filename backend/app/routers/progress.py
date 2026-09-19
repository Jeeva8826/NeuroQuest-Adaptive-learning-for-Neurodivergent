from fastapi import APIRouter, HTTPException, Depends
from app.models.progress import LearnerProgress
from app.database import get_database
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/api/progress", tags=["Progress"])

@router.get("/summary", response_model=LearnerProgress)
async def get_progress_summary(current_user: dict = Depends(get_current_user)):
    db = get_database()
    learner_id = current_user.get("learner_id") or current_user.get("active_learner_id")
    if not learner_id and current_user.get("id"):
        caretaker_id = str(current_user.get("id"))
        student = await db["students"].find_one({"caretaker_id": caretaker_id})
        if not student:
            student = await db["learners"].find_one({"$or": [{"caretaker_id": caretaker_id}, {"caregiver_id": caretaker_id}]})
        if student:
            learner_id = str(student.get("id", student.get("_id")))
    if not learner_id:
        learner_id = f"learner_{current_user.get('id', 'default')}"
        
    prog_doc = await db["progress"].find_one({"learner_id": learner_id})
    if not prog_doc:
        # Return default initialized structure
        badges = await db["rewards"].find().to_list(10)
        prog_doc = {
            "learner_id": learner_id,
            "total_stars": 10,
            "total_tasks_completed": 0,
            "streak_days": 1,
            "subject_mastery": {
                "Mathematics": 0,
                "Science": 0,
                "English": 0,
                "General Knowledge": 0,
                "Coding/Logic": 0
            },
            "earned_badges": badges,
            "unlocked_themes": ["space", "animals"]
        }
        await db["progress"].insert_one(prog_doc)
        
    return LearnerProgress(**prog_doc)
