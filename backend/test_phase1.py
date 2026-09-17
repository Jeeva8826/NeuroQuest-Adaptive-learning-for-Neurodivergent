from fastapi.testclient import TestClient
from app.main import app

def test_phase1_flow():
    # Use context manager so lifespan runs connect_to_mongo & seed_database_content
    with TestClient(app) as client:
        # 1. Root health check
        res = client.get("/")
        assert res.status_code == 200
        print("[OK] Backend health check passed.")

        # 2. Register Caregiver
        reg_payload = {
            "email": "caregiver_test@neuroquest.ai",
            "username": "caregiver_test",
            "password": "securepassword123",
            "full_name": "Test Caregiver",
            "role": "caregiver",
            "learner_name": "Leo",
            "learner_age": 9
        }
        reg_res = client.post("/api/auth/register", json=reg_payload)
        if reg_res.status_code != 200:
            # Try logging in if already created
            login_res = client.post("/api/auth/login", json={
                "email": reg_payload["email"],
                "password": reg_payload["password"]
            })
            assert login_res.status_code == 200
            token_data = login_res.json()
        else:
            token_data = reg_res.json()

        access_token = token_data["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        print("[OK] Auth registration/login passed.")

        # 3. Submit 24-Question Caregiver Questionnaire
        q_payload = {
            "q1_enjoyed_topics": "Black holes and space rockets",
            "q2_engaging_activities": "Building Lego space shuttles",
            "q3_themes": ["Space", "Coding/Technology"],
            "q4_hobbies": "Origami, Space videos",
            "q5_voluntary_subjects": "Astronomy",
            "q6_favorite_color": "purple",
            "q7_disliked_colors": ["bright red"],
            "q8_color_palette_preference": "Soft/muted colors",
            "q9_visual_style_preference": "Pictures",
            "q10_animation_effect": "distract",
            "q11_sound_effect": "help",
            "q12_prefer_calm_screen": True,
            "q13_prefer_movement": False,
            "q14_avoided_patterns": "Flashing lights",
            "q15_learning_modality": ["Seeing", "Doing"],
            "q16_task_structure": "Step-by-step guidance",
            "q17_difficulty_reaction": "needs_break",
            "q18_reengagement_helper": "visual_reward",
            "q19_feedback_style": "immediate",
            "q20_excitement_triggers": "Unlocking cosmic trophies",
            "q21_reward_types": ["Unlocking something", "Collecting objects"],
            "q22_frustration_triggers": "Harsh red wrong markers",
            "q23_calming_methods": "Soft ambient music",
            "q24_platform_avoidances": "Strict countdown timers"
        }

        q_res = client.post("/api/onboarding/questionnaire", json=q_payload, headers=headers)
        assert q_res.status_code == 200
        profile_data = q_res.json()
        assert profile_data["visual_preferences"]["background_theme"] == "space"
        assert profile_data["visual_preferences"]["primary_color"] == "#8b5cf6" # purple hex!
        print("[OK] Caregiver Questionnaire & Profile Engine passed.")

        # 4. Get Learner Profile
        prof_res = client.get("/api/learner/profile", headers=headers)
        assert prof_res.status_code == 200
        print("[OK] Learner profile retrieval passed.")

        # 5. Get Seed Tasks
        tasks_res = client.get("/api/tasks", headers=headers)
        assert tasks_res.status_code == 200
        tasks = tasks_res.json()
        assert len(tasks) > 0
        print(f"[OK] Seed tasks returned ({len(tasks)} tasks).")

        # 6. Start Learning Session
        start_res = client.post("/api/session/start", headers=headers)
        assert start_res.status_code == 200
        session = start_res.json()
        session_id = session["id"]

        # 7. Submit Task Answer
        task_id = tasks[0]["id"]
        correct_ans = tasks[0]["correct_answer"]
        ans_res = client.post(f"/api/session/{session_id}/answer", json={
            "task_id": task_id,
            "selected_answer": correct_ans,
            "time_taken_seconds": 12,
            "hints_used": 0
        }, headers=headers)
        assert ans_res.status_code == 200
        ans_data = ans_res.json()
        assert ans_data["is_correct"] is True
        assert ans_data["points_earned"] == 10
        print("[OK] Task answer & non-punitive scoring passed.")

        # 8. Update Theme Preferences Live
        update_res = client.put("/api/learner/preferences", json={
            "primary_color": "#10b981",
            "font_family": "dyslexic"
        }, headers=headers)
        assert update_res.status_code == 200
        updated_prof = update_res.json()
        assert updated_prof["visual_preferences"]["primary_color"] == "#10b981"
        assert updated_prof["visual_preferences"]["font_family"] == "dyslexic"
        print("[OK] Live preference theme customization passed.")

        # 9. Get Progress Summary
        prog_res = client.get("/api/progress/summary", headers=headers)
        assert prog_res.status_code == 200
        prog_data = prog_res.json()
        assert prog_data["total_stars"] >= 20
        print("[OK] Progress summary & rewards passed.")

        print("\nALL PHASE 1 INTEGRATION TESTS PASSED PERFECTLY!")

if __name__ == "__main__":
    test_phase1_flow()
