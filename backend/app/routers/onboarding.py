from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
from app.models.questionnaire import CaregiverQuestionnaireInput, CaregiverQuestionnaireResponse
from app.models.learner_profile import LearnerProfile
from app.database import get_database
from app.services.auth_service import get_current_user
from app.services.profile_engine import process_questionnaire_to_profile

router = APIRouter(prefix="/api/onboarding", tags=["Onboarding"])

@router.post("/questionnaire", response_model=LearnerProfile)
async def submit_questionnaire(
    questionnaire_input: CaregiverQuestionnaireInput,
    current_user: dict = Depends(get_current_user)
):
    db = get_database()
    caregiver_id = current_user["id"]
    learner_id = current_user.get("learner_id")
    
    if not learner_id:
        # Create a learner record if missing
        learner_doc = {
            "caregiver_id": caregiver_id,
            "name": f"{current_user['full_name']}'s Learner",
            "created_at": datetime.utcnow()
        }
        l_res = await db["learners"].insert_one(learner_doc)
        learner_id = str(l_res.inserted_id)
        await db["users"].update_one({"_id": current_user["_id"]}, {"$set": {"learner_id": learner_id}})

    # Get learner name
    learner_obj = await db["learners"].find_one({"_id": learner_id})
    learner_name = learner_obj.get("name", "Learner") if learner_obj else "Learner"

    # Save questionnaire responses to caregiver_profiles collection
    q_doc = questionnaire_input.model_dump()
    q_doc.update({
        "caregiver_id": caregiver_id,
        "learner_id": learner_id,
        "created_at": datetime.utcnow()
    })
    await db["caregiver_profiles"].insert_one(q_doc)

    # Process questionnaire to generate Learner Profile & Theme preferences
    profile = process_questionnaire_to_profile(
        questionnaire=questionnaire_input,
        learner_id=learner_id,
        caregiver_id=caregiver_id,
        learner_name=learner_name
    )

    profile_doc = profile.model_dump()
    profile_doc["updated_at"] = datetime.utcnow()

    # Save or update learner_preferences collection
    await db["learner_preferences"].update_one(
        {"learner_id": learner_id},
        {"$set": profile_doc},
        upsert=True
    )

    # Initialize progress record for learner if not exists
    existing_progress = await db["progress"].find_one({"learner_id": learner_id})
    if not existing_progress:
        # Seed progress with initial unlocked rewards
        badges = await db["rewards"].find().to_list(10)
        await db["progress"].insert_one({
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
            "unlocked_themes": ["space", "animals", profile.visual_preferences.background_theme],
            "last_active": datetime.utcnow()
        })

    return profile
