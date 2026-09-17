import sys
from fastapi.testclient import TestClient
from app.main import app

def test_final_hackathon_demo():
    print("==================================================")
    print("STARTING NEUROQUEST FINAL HACKATHON TEST SUITE")
    print("==================================================")

    with TestClient(app) as client:
        # 1. Fetch Demo Learner Profiles
        print("\n[1] Testing Demo Profiles Endpoint...")
        prof_res = client.get("/api/demo/profiles")
        assert prof_res.status_code == 200
        profiles = prof_res.json()["profiles"]
        assert len(profiles) == 3
        print(f"   -> Returned {len(profiles)} demo profiles: {[p['label'] for p in profiles]}")

        # 2. Authenticate Demo User
        reg_payload = {
            "email": "demo_judge@neuroquest.ai",
            "username": "demo_judge",
            "password": "securepassword123",
            "full_name": "Hackathon Judge User",
            "role": "caregiver",
            "learner_name": "Demo Learner",
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
        print("   -> Judge Auth token acquired.")

        # 3. Test Demo Learner A Activation (Space Theme, Visual Mode, Exploration)
        print("\n[2] Testing Demo Learner A Activation (Space & Exploration)...")
        act_a = client.post("/api/demo/activate-profile", json={"learner_id": "demo_learner_a"}, headers=headers)
        assert act_a.status_code == 200
        profile_a = act_a.json()["profile"]
        assert profile_a["visual_preferences"]["background_theme"] == "space"
        print(f"   -> Activated Learner A: Theme '{profile_a['visual_preferences']['background_theme']}', Reward Style '{profile_a['motivation']['reward_style']}'")

        # 4. Test Demo Learner B Activation (Animals Theme, Audio+Visual Mode, Collection)
        print("\n[3] Testing Demo Learner B Activation (Animals & Collection)...")
        act_b = client.post("/api/demo/activate-profile", json={"learner_id": "demo_learner_b"}, headers=headers)
        assert act_b.status_code == 200
        profile_b = act_b.json()["profile"]
        assert profile_b["visual_preferences"]["background_theme"] == "animals"
        print(f"   -> Activated Learner B: Theme '{profile_b['visual_preferences']['background_theme']}', Reward Style '{profile_b['motivation']['reward_style']}'")

        # 5. Test Demo Learner C Activation (Coding Theme, Interactive Mode, Building)
        print("\n[4] Testing Demo Learner C Activation (Coding & Building)...")
        act_c = client.post("/api/demo/activate-profile", json={"learner_id": "demo_learner_c"}, headers=headers)
        assert act_c.status_code == 200
        profile_c = act_c.json()["profile"]
        assert profile_c["visual_preferences"]["background_theme"] == "coding"
        print(f"   -> Activated Learner C: Theme '{profile_c['visual_preferences']['background_theme']}', Reward Style '{profile_c['motivation']['reward_style']}'")

        # 6. Test Judge State Simulation (FOCUSED, ATTENTION_DRIFT, POSSIBLE_FATIGUE)
        print("\n[5] Testing Judge State Simulation Mode...")
        sim_drift = client.post("/api/demo/simulate-state", json={"simulated_state": "ATTENTION_DRIFT"}, headers=headers)
        assert sim_drift.status_code == 200
        drift_data = sim_drift.json()
        assert drift_data["adaptation"]["uiMode"] == "focus"
        print(f"   -> State 'ATTENTION_DRIFT' simulated: UI Mode changed to '{drift_data['adaptation']['uiMode']}'")

        sim_fatigue = client.post("/api/demo/simulate-state", json={"simulated_state": "POSSIBLE_FATIGUE"}, headers=headers)
        assert sim_fatigue.status_code == 200
        fatigue_data = sim_fatigue.json()
        assert fatigue_data["adaptation"]["uiMode"] == "calm"
        print(f"   -> State 'POSSIBLE_FATIGUE' simulated: UI Mode changed to '{fatigue_data['adaptation']['uiMode']}'")

        # 7. Test Non-Medical Adaptation Explanation Endpoint
        print("\n[6] Testing Judge Adaptation Visualization Explainer...")
        expl_res = client.get("/api/demo/adaptation-explanation", headers=headers)
        assert expl_res.status_code == 200
        expl_data = expl_res.json()
        assert "adaptation_reasons" in expl_data
        print(f"   -> Adaptation Explainer returned {len(expl_data['adaptation_reasons'])} non-medical reasons.")

        # 8. Test Session Completion & Personal Game World Vault
        print("\n[7] Testing Learning Session Completion & Vault Storage...")
        start_res = client.post("/api/session/start", headers=headers)
        session_id = start_res.json()["id"]

        tasks_res = client.get("/api/tasks", headers=headers)
        task_id = tasks_res.json()[0]["id"]
        correct_ans = tasks_res.json()[0]["correct_answer"]

        ans_res = client.post(f"/api/session/{session_id}/answer", json={
            "task_id": task_id,
            "selected_answer": correct_ans,
            "time_taken_seconds": 12,
            "hints_used": 0
        }, headers=headers)
        assert ans_res.status_code == 200
        assert ans_res.json()["is_correct"] is True

        world_res = client.get("/api/game-world", headers=headers)
        assert world_res.status_code == 200
        print("   -> Personal game world and inventory updated successfully.")

    print("\n==================================================")
    print("ALL FINAL HACKATHON DEMO TESTS PASSED PERFECTLY!")
    print("==================================================")

if __name__ == "__main__":
    test_final_hackathon_demo()
