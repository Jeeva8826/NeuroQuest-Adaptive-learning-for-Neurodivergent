from fastapi.testclient import TestClient
from app.main import app
from app.ml.train_model import train_and_save_model
from app.ml.predict_service import predict_learner_state

def test_phase2_flow():
    # 1. Verify ML Training & Serialization
    print("[OK] Testing Scikit-Learn Model Training & Serialization...")
    model_data = train_and_save_model()
    assert model_data is not None
    assert model_data["accuracy"] > 0.85
    print(f"[OK] ML Model trained successfully with accuracy {model_data['accuracy'] * 100:.2f}%.")

    # 2. Test Predict Service for Different Feature Profiles
    print("[OK] Testing Learner State Classifier Predictions...")

    # Case A: Focused
    focused_pred = predict_learner_state({
        "has_gaze": True,
        "gaze_drift_std": 10.0,
        "gaze_offscreen_ratio": 0.02,
        "click_rate_per_min": 20.0,
        "rapid_click_count": 0,
        "idle_ratio": 0.1,
        "avg_response_time_sec": 5.0,
        "incorrect_attempt_count": 0,
        "hint_request_count": 0,
        "session_duration_mins": 5.0
    })
    print(f"   -> Focused Profile Result: {focused_pred['state_name']} (Confidence: {focused_pred['confidence']})")

    # Case B: Possible Fatigue
    fatigue_pred = predict_learner_state({
        "has_gaze": True,
        "gaze_drift_std": 50.0,
        "gaze_offscreen_ratio": 0.3,
        "click_rate_per_min": 8.0,
        "rapid_click_count": 3,
        "idle_ratio": 0.6,
        "avg_response_time_sec": 35.0,
        "incorrect_attempt_count": 2,
        "hint_request_count": 1,
        "session_duration_mins": 40.0
    })
    print(f"   -> Fatigue Profile Result: {fatigue_pred['state_name']} (Confidence: {fatigue_pred['confidence']})")

    # Case C: Non-camera Telemetry Fallback
    non_cam_pred = predict_learner_state({
        "has_gaze": False, # Camera denied or unavailable
        "click_rate_per_min": 15.0,
        "rapid_click_count": 0,
        "idle_ratio": 0.15,
        "avg_response_time_sec": 7.0,
        "session_duration_mins": 10.0
    })
    assert non_cam_pred["has_camera_gaze"] is False
    print(f"   -> Non-Camera Fallback Result: {non_cam_pred['state_name']} (Confidence: {non_cam_pred['confidence']})")

    # 3. Test Telemetry FastAPI Endpoint via TestClient
    with TestClient(app) as client:
        # Register Caregiver
        reg_res = client.post("/api/auth/register", json={
            "email": "caregiver_p2@neuroquest.ai",
            "username": "caregiver_p2",
            "password": "securepassword123",
            "full_name": "Phase 2 Caregiver",
            "role": "caregiver",
            "learner_name": "Maya",
            "learner_age": 8
        })
        if reg_res.status_code != 200:
            login_res = client.post("/api/auth/login", json={
                "email": "caregiver_p2@neuroquest.ai",
                "password": "securepassword123"
            })
            token_data = login_res.json()
        else:
            token_data = reg_res.json()

        headers = {"Authorization": f"Bearer {token_data['access_token']}"}

        # Onboarding
        client.post("/api/onboarding/questionnaire", json={
            "q1_enjoyed_topics": "Animals & Nature",
            "q2_engaging_activities": "Drawing cats",
            "q3_themes": ["Animals", "Nature"],
            "q4_hobbies": "Drawing",
            "q5_voluntary_subjects": "Biology",
            "q6_favorite_color": "teal",
            "q7_disliked_colors": [],
            "q8_color_palette_preference": "Soft/muted colors",
            "q9_visual_style_preference": "Pictures",
            "q10_animation_effect": "distract",
            "q11_sound_effect": "distract",
            "q12_prefer_calm_screen": True,
            "q13_prefer_movement": False,
            "q14_avoided_patterns": "",
            "q15_learning_modality": ["Seeing", "Doing"],
            "q16_task_structure": "Step-by-step guidance",
            "q17_difficulty_reaction": "needs_break",
            "q18_reengagement_helper": "visual_reward",
            "q19_feedback_style": "immediate",
            "q20_excitement_triggers": "Animal badges",
            "q21_reward_types": ["Collecting objects"],
            "q22_frustration_triggers": "",
            "q23_calming_methods": "",
            "q24_platform_avoidances": ""
        }, headers=headers)

        # Start Session
        s_res = client.post("/api/session/start", headers=headers)
        session_id = s_res.json()["id"]

        # Evaluate Telemetry
        eval_res = client.post("/api/telemetry/evaluate", json={
            "session_id": session_id,
            "has_gaze": True,
            "gaze_drift_std": 60.0,
            "gaze_offscreen_ratio": 0.4,
            "click_rate_per_min": 6.0,
            "rapid_click_count": 2,
            "idle_ratio": 0.65,
            "avg_response_time_sec": 45.0,
            "incorrect_attempt_count": 2,
            "hint_request_count": 1,
            "session_duration_mins": 35.0,
            "current_difficulty": 3
        }, headers=headers)

        assert eval_res.status_code == 200
        eval_data = eval_res.json()
        assert "state" in eval_data
        assert "adaptation" in eval_data
        assert eval_data["adaptation"]["uiMode"] in ["calm", "focus", "minimal", "normal"]
        print(f"[OK] Telemetry evaluation API returned state '{eval_data['state']['state_name']}' and recommended UI mode '{eval_data['adaptation']['uiMode']}'.")

        # Get Caregiver Insights
        cg_res = client.get("/api/caregiver/insights", headers=headers)
        assert cg_res.status_code == 200
        cg_data = cg_res.json()
        assert "engagement_distribution" in cg_data
        assert "effective_adaptations" in cg_data
        print(f"[OK] Caregiver Insights API returned valid non-medical dashboard metrics.")

    print("\nALL PHASE 2 INTEGRATION TESTS PASSED PERFECTLY!")

if __name__ == "__main__":
    test_phase2_flow()
