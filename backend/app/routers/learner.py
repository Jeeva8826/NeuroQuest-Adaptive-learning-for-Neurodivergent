from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
from app.models.learner_profile import LearnerProfile, PreferenceUpdateRequest
from app.database import get_database
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/api/learner", tags=["Learner"])

@router.get("/profile", response_model=LearnerProfile)
async def get_learner_profile(current_user: dict = Depends(get_current_user)):
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
        
    profile_doc = await db["learner_preferences"].find_one({"learner_id": learner_id})
    if not profile_doc:
        default_profile = {
            "learner_id": learner_id,
            "caregiver_id": current_user.get("id", ""),
            "learner_name": current_user.get("full_name", "Explorer"),
            "interests": ["Space", "Animals"],
            "visual_preferences": {
                "primary_color": "#2563EB",
                "secondary_color": "#38BDF8",
                "palette_type": "soft",
                "background_theme": "space",
                "font_family": "OpenDyslexic",
                "font_scale": "medium"
            },
            "sensory_preferences": {
                "animation_intensity": "gentle",
                "sound_enabled": True,
                "visual_density": "low"
            },
            "interaction_preferences": {
                "task_size": "small",
                "guidance_level": "high"
            },
            "motivation_preferences": {
                "reward_type": "stars",
                "collectible_theme": "space_badges"
            },
            "created_at": datetime.utcnow()
        }
        ins = await db["learner_preferences"].insert_one(default_profile)
        default_profile["id"] = str(ins.inserted_id)
        default_profile["_id"] = str(ins.inserted_id)
        return default_profile
        
    profile_doc["id"] = str(profile_doc["_id"])
    profile_doc["_id"] = str(profile_doc["_id"])
    return profile_doc

@router.get("s/{learner_id}/profile")
async def get_learner_by_id_profile(learner_id: str):
    db = get_database()
    profile_doc = await db["learner_preferences"].find_one({"learner_id": learner_id})
    if not profile_doc:
        return {"learner_id": learner_id, "visual_preferences": {"background_theme": "space"}}
    profile_doc["id"] = str(profile_doc.get("_id", ""))
    if "_id" in profile_doc:
        profile_doc["_id"] = str(profile_doc["_id"])
    return profile_doc

@router.put("/preferences", response_model=LearnerProfile)
async def update_learner_preferences(
    update_req: PreferenceUpdateRequest,
    current_user: dict = Depends(get_current_user)
):
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
        
    profile_doc = await db["learner_preferences"].find_one({"learner_id": learner_id})
    if not profile_doc:
        await db["learner_preferences"].insert_one({
            "learner_id": learner_id,
            "visual_preferences": {},
            "sensory_preferences": {},
            "interaction_preferences": {}
        })
        profile_doc = await db["learner_preferences"].find_one({"learner_id": learner_id})
        
    # Update fields in visual_preferences, sensory_preferences, or interaction_preferences
    vis = profile_doc.get("visual_preferences", {})
    sen = profile_doc.get("sensory_preferences", {})
    inter = profile_doc.get("interaction_preferences", {})

    if update_req.primary_color:
        vis["primary_color"] = update_req.primary_color
    if update_req.secondary_color:
        vis["secondary_color"] = update_req.secondary_color
    if update_req.palette_type:
        vis["palette_type"] = update_req.palette_type
    if update_req.background_theme:
        vis["background_theme"] = update_req.background_theme
    if update_req.font_family:
        vis["font_family"] = update_req.font_family
    if update_req.font_scale:
        vis["font_scale"] = update_req.font_scale

    if update_req.animation_intensity:
        sen["animation_intensity"] = update_req.animation_intensity
    if update_req.sound_enabled is not None:
        sen["sound_enabled"] = update_req.sound_enabled
    if update_req.visual_density:
        sen["visual_density"] = update_req.visual_density

    if update_req.task_size:
        inter["task_size"] = update_req.task_size
    if update_req.guidance_level:
        inter["guidance_level"] = update_req.guidance_level

    await db["learner_preferences"].update_one(
        {"learner_id": learner_id},
        {
            "$set": {
                "visual_preferences": vis,
                "sensory_preferences": sen,
                "interaction_preferences": inter,
                "updated_at": datetime.utcnow()
            }
        }
    )

    updated_profile = await db["learner_preferences"].find_one({"learner_id": learner_id})
    updated_profile["id"] = str(updated_profile["_id"])
    updated_profile["_id"] = str(updated_profile["_id"])
    return updated_profile
