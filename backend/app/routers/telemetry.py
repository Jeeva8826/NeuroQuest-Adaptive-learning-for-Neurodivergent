from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from app.models.session import LearningEvent
from app.database import get_database
from app.services.auth_service import get_current_user
from app.ml.predict_service import predict_learner_state
from app.services.adaptation_engine import compute_session_adaptations

router = APIRouter(prefix="/api/telemetry", tags=["Telemetry"])

class TelemetryPayload(BaseModel):
    session_id: str
    has_gaze: bool = False
    gaze_drift_std: float = 15.0
    gaze_offscreen_ratio: float = 0.0
    click_rate_per_min: float = 15.0
    rapid_click_count: int = 0
    idle_ratio: float = 0.1
    avg_response_time_sec: float = 8.0
    incorrect_attempt_count: int = 0
    hint_request_count: int = 0
    session_duration_mins: float = 5.0
    current_difficulty: int = 2

@router.post("/evaluate")
async def evaluate_telemetry(
    payload: TelemetryPayload,
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

    # 1. Fetch Learner Preference Profile
    profile_doc = await db["learner_preferences"].find_one({"learner_id": learner_id})
    if not profile_doc:
        profile_doc = {
            "visual_preferences": {"primary_color": "#3b82f6", "background_theme": "space"},
            "sensory_preferences": {},
            "interaction_preferences": {},
            "interests": ["Space", "Exploration"]
        }

    # 2. Predict Learner Interaction State using Scikit-Learn ML
    telemetry_dict = payload.model_dump()
    state_result = predict_learner_state(telemetry_dict)

    # 3. Compute Session UI & Content Adaptations
    adaptation_result = compute_session_adaptations(
        learner_profile=profile_doc,
        predicted_state_data=state_result,
        current_difficulty=payload.current_difficulty
    )

    # 4. Log telemetry event & state update to MongoDB
    event_doc = {
        "learner_id": learner_id,
        "session_id": payload.session_id,
        "event_type": "state_evaluation",
        "payload": {
            "predicted_state": state_result["state_name"],
            "confidence": state_result["confidence"],
            "has_camera_gaze": payload.has_gaze,
            "ui_mode": adaptation_result["uiMode"],
            "difficulty_adjustment": adaptation_result["difficultyAdjustment"]
        },
        "timestamp": datetime.utcnow()
    }
    await db["learning_events"].insert_one(event_doc)

    # 5. Persist live learner profile state
    await db["learner_profile_state"].update_one(
        {"learner_id": learner_id},
        {
            "$set": {
                "current_state": state_result["state_name"],
                "last_active_session": payload.session_id,
                "current_ui_mode": adaptation_result["uiMode"],
                "updated_at": datetime.utcnow()
            }
        },
        upsert=True
    )

    return {
        "state": state_result,
        "adaptation": adaptation_result
    }
