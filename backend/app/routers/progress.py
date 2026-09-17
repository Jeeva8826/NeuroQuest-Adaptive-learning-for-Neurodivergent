from fastapi import APIRouter, HTTPException, Depends
from app.models.progress import LearnerProgress
from app.database import get_database
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/api/progress", tags=["Progress"])

@router.get("/summary", response_model=LearnerProgress)
async def get_progress_summary(current_user: dict = Depends(get_current_user)):
    db = get_database()
    learner_id = current_user.get("learner_id")
    if not learner_id:
        raise HTTPException(status_code=404, detail="No learner ID found.")
        
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
