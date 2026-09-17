import sys
from fastapi.testclient import TestClient
from app.main import app
from app.services.interest_engine import interest_engine
from app.services.adaptive_difficulty import adaptive_difficulty_engine

def test_phase3_flow():
    print("==================================================")
    print("STARTING NEUROQUEST PHASE 3 INTEGRATION TEST SUITE")
    print("==================================================")

    # 1. Test Interest Engine Mapping (Predefined & Custom Text)
    print("\n[1] Testing Interest-to-Game Engine Mapping...")
    space_theme = interest_engine.resolve_theme(["space exploration"])
    assert space_theme["theme_id"] == "space"
    assert space_theme["hero_role"] == "Commander"

    dino_theme = interest_engine.resolve_theme(["rollercoasters and physics"])
    assert dino_theme["world_name"] == "Rollercoasters and physics World"
    print("[OK] Interest Mapping Engine mapped standard and custom interest text correctly.")

    # 2. Test Adaptive Difficulty Policy
    print("\n[2] Testing Adaptive Difficulty Engine...")
    inc_diff = adaptive_difficulty_engine.evaluate_next_difficulty(
        current_difficulty=1, accuracy_rate=0.9, avg_response_time_sec=10.0,
        hint_count=0, attempt_count=1, session_state="FOCUSED", consecutive_correct=3
    )
    assert inc_diff["new_difficulty"] == 2
    assert inc_diff["action"] == "increase"

    dec_diff = adaptive_difficulty_engine.evaluate_next_difficulty(
        current_difficulty=3, accuracy_rate=0.3, avg_response_time_sec=50.0,
        hint_count=2, attempt_count=3, session_state="POSSIBLE_FATIGUE", consecutive_errors=2
    )
    assert dec_diff["new_difficulty"] == 2
    assert dec_diff["action"] == "decrease"
    print("[OK] Adaptive Difficulty Engine successfully adjusted levels based on learner metrics.")

    # 3. Test End-to-End API Flow via FastAPI TestClient
    print("\n[3] Testing End-to-End Phase 3 API Flow...")
    with TestClient(app) as client:
        # Register Caregiver
        reg_payload = {
            "email": "phase3_learner@neuroquest.ai",
            "username": "phase3_learner",
            "password": "securepassword123",
            "full_name": "Phase 3 Caregiver",
            "role": "caregiver",
            "learner_name": "Aria",
            "learner_age": 10
        }
        reg_res = client.post("/api/auth/register", json=reg_payload)
        if reg_res.status_code != 200:
            login_res = client.post("/api/auth/login", json={
                "email": reg_payload["email"],
                "password": reg_payload["password"]
            })
            token_data = login_res.json()
        else:
            token_data = reg_res.json()

        headers = {"Authorization": f"Bearer {token_data['access_token']}"}

        # Onboarding Questionnaire
        q_res = client.post("/api/onboarding/questionnaire", json={
            "q1_enjoyed_topics": "Robots & Space Station",
            "q2_engaging_activities": "Building coding robots",
            "q3_themes": ["Coding/Technology", "Space"],
            "q4_hobbies": "Robot programming",
            "q5_voluntary_subjects": "Coding",
            "q6_favorite_color": "indigo",
            "q7_disliked_colors": [],
            "q8_color_palette_preference": "Soft/muted colors",
            "q9_visual_style_preference": "Pictures",
            "q10_animation_effect": "help",
            "q11_sound_effect": "help",
            "q12_prefer_calm_screen": True,
            "q13_prefer_movement": False,
            "q14_avoided_patterns": "",
            "q15_learning_modality": ["Seeing", "Doing"],
            "q16_task_structure": "Step-by-step guidance",
            "q17_difficulty_reaction": "needs_break",
            "q18_reengagement_helper": "visual_reward",
            "q19_feedback_style": "immediate",
            "q20_excitement_triggers": "Unlocking robot parts",
            "q21_reward_types": ["Collecting objects", "Unlocking something"],
            "q22_frustration_triggers": "Harsh wrong markers",
            "q23_calming_methods": "Soft chimes",
            "q24_platform_avoidances": "Timers"
        }, headers=headers)
        assert q_res.status_code == 200
        print("   -> Caregiver Onboarding complete.")

        # Test Daily Return Welcome Experience API
        welcome_res = client.get("/api/ai/daily-welcome", headers=headers)
        assert welcome_res.status_code == 200
        w_data = welcome_res.json()
        assert "greeting" in w_data
        assert "mission_title" in w_data
        print(f"   -> Daily Return Welcome API: '{w_data['mission_title']}'")

        # Test AI Mentor Personalized Task Generation
        gen_res = client.post("/api/ai/personalized-task", json={
            "subject": "Coding/Logic",
            "difficulty": 2,
            "base_objective": "Program robot maze turns"
        }, headers=headers)
        assert gen_res.status_code == 200
        gen_data = gen_res.json()
        assert "title" in gen_data
        assert "question" in gen_data
        print(f"   -> Personalized Task Generated: Title '{gen_data['title']}'")

        # Test AI Gentle Hint & Failure Scaffolding API
        hint_res = client.post("/api/ai/hint", json={
            "question": gen_data["question"],
            "correct_answer": gen_data["correct_answer"],
            "attempt_count": 1
        }, headers=headers)
        assert hint_res.status_code == 200
        print(f"   -> AI Mentor Hint API: '{hint_res.json()['hint']}'")

        scaffold_res = client.post("/api/ai/scaffold", json={
            "task": gen_data,
            "attempt_count": 2
        }, headers=headers)
        assert scaffold_res.status_code == 200
        sc_data = scaffold_res.json()
        assert sc_data["next_representation"] == "visual_block"
        print(f"   -> Failure Scaffolding API: Action '{sc_data['action']}', Representation '{sc_data['next_representation']}'")

        # Test Personal Game World & Mastery Tree API
        world_res = client.get("/api/game-world", headers=headers)
        assert world_res.status_code == 200
        world_data = world_res.json()
        assert "world_name" in world_data
        assert "inventory" in world_data
        print(f"   -> Personal Game World API: '{world_data['world_name']}' (Role: {world_data['hero_role']})")

        tree_res = client.get("/api/game-world/mastery-tree", headers=headers)
        assert tree_res.status_code == 200
        tree_data = tree_res.json()
        assert len(tree_data["nodes"]) > 0
        print(f"   -> Personal Mastery Tree API returned {len(tree_data['nodes'])} skill nodes.")

        # Test Session Answer Submission with Personalized Rewards
        start_session_res = client.post("/api/session/start", headers=headers)
        session_id = start_session_res.json()["id"]

        tasks_res = client.get("/api/tasks", headers=headers)
        task_id = tasks_res.json()[0]["id"]
        correct_ans = tasks_res.json()[0]["correct_answer"]

        ans_res = client.post(f"/api/session/{session_id}/answer", json={
            "task_id": task_id,
            "selected_answer": correct_ans,
            "time_taken_seconds": 10,
            "hints_used": 0
        }, headers=headers)
        assert ans_res.status_code == 200
        ans_data = ans_res.json()
        assert ans_data["is_correct"] is True
        assert "personalized_reward" in ans_data
        msg = ans_data['personalized_reward']['message'].encode('ascii', 'ignore').decode('ascii')
        print(f"   -> Session Task Answer API returned reward message: '{msg}'")

    print("\n==================================================")
    print("ALL PHASE 3 INTEGRATION TESTS PASSED PERFECTLY!")
    print("==================================================")

if __name__ == "__main__":
    test_phase3_flow()
