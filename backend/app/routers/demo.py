from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from app.services.auth_service import get_current_user
from app.database import get_database
from app.services.seed_service import DEMO_PROFILES
from app.services.adaptation_explainer import adaptation_explainer_service
from app.services.adaptation_engine import compute_session_adaptations

router = APIRouter(prefix="/api/demo", tags=["Hackathon Demo Simulation Mode"])

class ActivateProfileRequest(BaseModel):
    learner_id: str # demo_learner_a, demo_learner_b, demo_learner_c

class SimulateStateRequest(BaseModel):
    simulated_state: str # FOCUSED, ATTENTION_DRIFT, POSSIBLE_FATIGUE, HIGH_ENGAGEMENT

@router.get("/profiles")
async def get_demo_profiles():
    """Returns the 3 distinct demo learner profiles for hackathon presentation."""
    return {
        "profiles": [
            {
                "id": "demo_learner_a",
                "label": "Learner A (Leo)",
                "interest": "Space & Rockets",
                "learning_mode": "Visual",
                "motivation": "Exploration Map",
                "description": "Space exploration theme, visual presentation, area unlock rewards."
            },
            {
                "id": "demo_learner_b",
                "label": "Learner B (Maya)",
                "interest": "Animals & Nature",
                "learning_mode": "Audio + Visual",
                "motivation": "Collection Vault",
                "description": "Wildlife sanctuary theme, audio-supported guidance, animal card rewards."
            },
            {
                "id": "demo_learner_c",
                "label": "Learner C (Kai)",
                "interest": "Coding & Robots",
                "learning_mode": "Interactive",
                "motivation": "Building Workshop",
                "description": "Cyber workshop theme, interactive logic maze, robot part rewards."
            }
        ]
    }

@router.post("/activate-profile")
async def activate_demo_profile(
    req: ActivateProfileRequest,
    current_user: dict = Depends(get_current_user)
):
    """Switches active learner profile to Demo Learner A, B, or C."""
    db = get_database()
    user_id = current_user.get("user_id")

    target_profile = next((p for p in DEMO_PROFILES if p["learner_id"] == req.learner_id), None)
    if not target_profile:
        raise HTTPException(status_code=404, detail="Demo profile not found.")

    # Link user to chosen demo learner profile
    await db["users"].update_one(
        {"_id": user_id},
        {"$set": {"learner_id": req.learner_id, "learner_name": target_profile["learner_name"]}}
    )

    # Upsert learner preferences
    profile_data = target_profile.copy()
    await db["learner_preferences"].update_one(
        {"learner_id": req.learner_id},
        {"$set": profile_data},
        upsert=True
    )

    return {
        "status": "success",
        "active_learner_id": req.learner_id,
        "profile": profile_data
    }

@router.post("/simulate-state")
async def simulate_learner_state(
    req: SimulateStateRequest,
    current_user: dict = Depends(get_current_user)
):
    """Simulates a learner behavioral state for judge demonstration."""
    db = get_database()
    learner_id = current_user.get("learner_id", "demo_learner_a")

    profile_doc = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}
    
    state_result = {
        "state_name": req.simulated_state,
        "confidence": 0.98,
        "simulated": True,
        "has_camera_gaze": True
    }

    adaptation_result = compute_session_adaptations(
        learner_profile=profile_doc,
        predicted_state_data=state_result,
        current_difficulty=2
    )

    # Persist live state
    await db["learner_profile_state"].update_one(
        {"learner_id": learner_id},
        {
            "$set": {
                "current_state": req.simulated_state,
                "current_ui_mode": adaptation_result["uiMode"],
                "updated_at": datetime.utcnow()
            }
        },
        upsert=True
    )

    explainer = adaptation_explainer_service.explain_adaptations(
        learner_profile=profile_doc,
        predicted_state_data=state_result,
        adaptation_result=adaptation_result
    )

    return {
        "simulated_state": req.simulated_state,
        "state": state_result,
        "adaptation": adaptation_result,
        "explainer": explainer
    }

@router.get("/adaptation-explanation")
async def get_adaptation_explanation(current_user: dict = Depends(get_current_user)):
    """Returns non-medical judge-facing adaptation explanation."""
    db = get_database()
    learner_id = current_user.get("learner_id", "demo_learner_a")
    profile = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}
    state_doc = await db["learner_profile_state"].find_one({"learner_id": learner_id}) or {}

    state_result = {"state_name": state_doc.get("current_state", "FOCUSED"), "confidence": 0.95}
    adaptation_result = compute_session_adaptations(
        learner_profile=profile,
        predicted_state_data=state_result
    )

    explainer = adaptation_explainer_service.explain_adaptations(
        learner_profile=profile,
        predicted_state_data=state_result,
        adaptation_result=adaptation_result
    )

    return explainer
