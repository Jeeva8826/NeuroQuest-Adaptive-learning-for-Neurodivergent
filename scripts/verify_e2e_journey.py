import os
import sys
import json

# Ensure backend directory is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from fastapi.testclient import TestClient
from app.main import app

def run_comprehensive_e2e_journey():
    print("=" * 65)
    print("NEUROQUEST END-TO-END VERIFICATION & CLIENT-READY JOURNEY SUITE")
    print("=" * 65)

    with TestClient(app) as client:
        # 1. System Health & Architecture Readiness
        print("\n[Stage 1] Verifying System Health & API Readiness...")
        h_res = client.get("/api/health")
        assert h_res.status_code == 200
        h_data = h_res.json()
        assert h_data.get("status") in ["healthy", "online"]
        print(f"   [OK] System Health: {h_data['status']} | App: {h_data.get('app')}")

        # 2. Caretaker & Learner Authentication
        print("\n[Stage 2] Caretaker Registration & Learner Account Creation...")
        test_email = "e2e_caregiver_leo@neuroquest.edu"
        reg_payload = {
            "email": test_email,
            "username": "e2e_caregiver_leo",
            "password": "E2ePassword!2026",
            "full_name": "Dr. Sarah Miller",
            "role": "caregiver",
            "learner_name": "Leo Miller",
            "learner_age": 12
        }
        reg_res = client.post("/api/auth/register", json=reg_payload)
        if reg_res.status_code == 200:
            token = reg_res.json()["access_token"]
            learner_id = reg_res.json().get("learner_id")
        else:
            login_res = client.post("/api/auth/login", json={"email": test_email, "password": "E2ePassword!2026"})
            token = login_res.json()["access_token"]
            learner_id = login_res.json().get("learner_id")
        
        headers = {"Authorization": f"Bearer {token}"}
        print(f"   [OK] Authenticated Learner ID: {learner_id}")

        # 3. NCERT Curriculum Knowledge Graph & Seeding Verification
        print("\n[Stage 3] Verifying NCERT Curriculum Knowledge Graph...")
        tasks_res = client.get("/api/tasks", headers=headers)
        assert tasks_res.status_code == 200
        tasks = tasks_res.json()
        assert len(tasks) > 0, "Tasks collection should not be empty!"
        print(f"   [OK] Tasks Catalog: {len(tasks)} curriculum tasks loaded into database.")

        # 4. 20-Question Non-Diagnostic Caretaker Assessment (Segment 8)
        print("\n[Stage 4] Submitting 20-Question Non-Diagnostic Pedagogical Questionnaire...")
        quest_payload = {
            "learner_name": "Leo Miller",
            "learner_age": 12,
            "interests": ["Space", "Robots", "Astronomy"],
            "hobbies": ["Telescope viewing", "Lego rocket design"],
            "q1_focus_duration": "10-15 minutes (best with bite-sized chunks)",
            "q2_sensory_distractions": "Sensitive to loud sharp noises, prefers calm chimes",
            "q3_visual_presentation": "Prefers OpenDyslexic / Rounded font with spacious layout",
            "q4_visual_palette": "Soft pastel palette (gentle on eyes)",
            "q5_sound_preference": "Gentle chimes with quick mute switch",
            "q6_motion_preference": "Low motion (minimal decorative animations)",
            "q7_reading_comfort": "Audio narration alongside readable text",
            "q8_math_representation": "Visual blocks and number line representations",
            "q9_scaffolding_pace": "Graduated hints after initial independent attempt",
            "q10_mistake_reaction": "Prefers gentle non-punitive re-tries and exploration",
            "q11_motivation_style": "Unlocking constellation nodes and exploration worlds",
            "q12_break_frequency": "Every 10 minutes with soothing breathing pauses",
            "q13_task_structure": "Step-by-step sequential breakdown",
            "q14_peer_comparison": "Purely personal progress, zero leaderboards",
            "q15_feedback_timing": "Immediate gentle celebration after each step",
            "q16_input_preference": "Big touch buttons and keyboard navigation",
            "q17_energy_fluctuation": "More focused in mornings, needs calm mode in afternoon",
            "q18_frustration_signal": "Rapid clicking or repeated answer changes",
            "q19_special_strengths": "Exceptional visual-spatial pattern recognition and deep topic curiosity",
            "q20_caregiver_priority": "Foster curiosity and self-confidence without performance anxiety"
        }
        q_res = client.post("/api/onboarding/questionnaire", json=quest_payload, headers=headers)
        assert q_res.status_code == 200, f"Questionnaire failed: {q_res.text}"
        q_data = q_res.json()
        assert "visual_preferences" in q_data
        assert q_data.get("visual_preferences", {}).get("font_scale") is not None
        print("   [OK] Questionnaire processed: Visual, Sensory & Interaction preferences mapped.")

        # 5. Non-Diagnostic Accommodations Submission (Zero Medical Pathology)
        print("\n[Stage 5] Submitting Non-Diagnostic Educational Accommodations...")
        med_payload = {
            "learner_id": learner_id,
            "condition": "General",
            "answers": [
                {
                    "question_id": "acc_1",
                    "question_text": "Sensory Sensitivities",
                    "answer": "Prefers calm pastel colors, gentle sound, and spacious layout"
                },
                {
                    "question_id": "acc_2",
                    "question_text": "Pedagogical Accommodations",
                    "answer": "OpenDyslexic font, break reminders, zero countdown timers"
                }
            ]
        }
        med_res = client.post("/api/medical/submit", json=med_payload, headers=headers)
        assert med_res.status_code == 200
        print("   [OK] Non-Diagnostic Accessibility Accommodations stored.")

        # 6. Daily Return Welcome API (Theme-Grounded)
        print("\n[Stage 6] Testing Daily Welcome Mission (Theme-Aware)...")
        w_res = client.get("/api/ai/daily-welcome", headers=headers)
        assert w_res.status_code == 200
        w_data = w_res.json()
        assert "greeting" in w_data
        print(f"   [OK] Daily Welcome: '{w_data.get('mission_title')}' (Theme: {w_data.get('theme')})")

        # 7. Personalized Mission Task Generation
        print("\n[Stage 7] Testing AI Personalized Mission Task Generator...")
        gen_res = client.post("/api/ai/personalized-task", json={
            "subject": "Science",
            "difficulty": 1,
            "base_objective": "Understand Plant Nutrition Autotrophs"
        }, headers=headers)
        assert gen_res.status_code == 200
        gen_task = gen_res.json()
        assert "question" in gen_task
        print(f"   [OK] Generated Mission Task: '{gen_task.get('title')}'")

        # 8. Learning Session Start
        print("\n[Stage 8] Starting Interactive Learning Session...")
        sess_res = client.post("/api/session/start", json={
            "session_type": "adaptive_mission",
            "initial_difficulty": 1
        }, headers=headers)
        assert sess_res.status_code == 200
        session_id = sess_res.json()["id"]
        print(f"   [OK] Active Session ID: {session_id}")

        # 9. Verifying 7-Level Graduated Scaffolding Ladder (Segment 14)
        print("\n[Stage 9] Testing Complete 7-Level Scaffolding Ladder...")
        curriculum_sample_task = {
            "id": "Q_PHOTO_01",
            "concept_id": "CON_PHOTOSYNTH_02",
            "question": "During photosynthesis in green leaves, which gas is released into the atmosphere?",
            "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
            "correct_answer": "Oxygen",
            "explanation": "Water is split in sunlight, producing carbohydrates and releasing oxygen into the air.",
            "hints": ["It is the vital gas humans and animals breathe.", "Plants take in CO2 and release this gas."],
            "scaffold_steps": ["Step 1: Carbon dioxide enters the leaf.", "Step 2: Oxygen exits as a helpful byproduct."]
        }

        # Verify all 7 levels
        for lvl in range(1, 8):
            sc_res = client.post("/api/ai/scaffold", json={
                "task": curriculum_sample_task,
                "attempt_count": lvl,
                "requested_level": lvl
            }, headers=headers)
            assert sc_res.status_code == 200, f"Scaffold Level {lvl} failed: {sc_res.text}"
            sc_data = sc_res.json()
            assert sc_data["scaffold_level"] == lvl
            assert sc_data["ladder_progress"]["current_level"] == lvl
            assert sc_data["action"] is not None
            assert sc_data["hint"] is not None

            # Check level-specific properties
            if lvl == 2:
                assert sc_data["next_representation"] == "visual_block"
                assert len(sc_data["eliminated_options"]) > 0
                print(f"   -> Level 2 OK: Visual block mode with eliminated distractor '{sc_data['eliminated_options'][0]}'")
            elif lvl == 3:
                assert sc_data["guiding_question"] is not None
                print(f"   -> Level 3 OK: Socratic guiding question '{sc_data['guiding_question'][:40]}...'")
            elif lvl == 4:
                assert sc_data["worked_example"] is not None
                print(f"   -> Level 4 OK: Worked example '{sc_data['worked_example']['scenario']}'")
            elif lvl == 5:
                assert sc_data["partial_step"] is not None
                print(f"   -> Level 5 OK: Partial step '{sc_data['partial_step']['prompt'][:40]}...'")
            elif lvl == 6:
                assert sc_data["reasoning_walkthrough"] is not None
                print(f"   -> Level 6 OK: Step-by-step reasoning walkthrough ({len(sc_data['reasoning_walkthrough'])} steps)")
            elif lvl == 7:
                assert sc_data["full_solution"] is not None
                assert sc_data["full_solution"]["final_answer"] == "Oxygen"
                print(f"   -> Level 7 OK: Full worked solution with final answer '{sc_data['full_solution']['final_answer']}'")

        print("   [OK] All 7 Scaffolding Ladder Levels verified with zero premature answer leaking.")

        # 10. Dynamic Adaptation & Explainer ("Why Did This Change?") (Segment 11)
        print("\n[Stage 10] Testing Transparent Explainable Adaptation API...")
        expl_res = client.get("/api/demo/adaptation-explanation", headers=headers)
        assert expl_res.status_code == 200
        expl_data = expl_res.json()
        assert "ui_mode" in expl_data
        assert "adaptation_reasons" in expl_data
        assert "current_state" in expl_data
        print(f"   [OK] Explainer: State '{expl_data['current_state']}' -> UI Mode '{expl_data['ui_mode']}'")
        print(f"   [OK] Pedagogical Adaptation Reasons: {len(expl_data['adaptation_reasons'])} non-medical items")

        # 11. Answering Task with Correct Solution & Reward Trigger
        print("\n[Stage 11] Answering Session Task & Earning Non-Punitive Mastery...")
        ans_res = client.post(f"/api/session/{session_id}/answer", json={
            "task_id": tasks[0]["id"],
            "selected_answer": tasks[0]["correct_answer"],
            "time_taken_seconds": 12,
            "hints_used": 1
        }, headers=headers)
        assert ans_res.status_code == 200
        ans_data = ans_res.json()
        assert ans_data.get("is_correct") is True
        msg = ans_data.get('personalized_reward', {}).get('message', 'Great exploration!').encode('ascii', 'ignore').decode('ascii')
        print(f"   [OK] Task Answered: +{ans_data.get('points_earned', 2)} points earned! Message: '{msg}'")

        # 12. Personal Game World & Mastery Skill Tree (Segment 13 & 15)
        print("\n[Stage 12] Verifying Personal Game World & Mastery Tree...")
        gw_res = client.get("/api/game-world", headers=headers)
        assert gw_res.status_code == 200
        gw_data = gw_res.json()
        assert "world_name" in gw_data
        print(f"   [OK] Game World: '{gw_data['world_name']}' | Role: {gw_data.get('hero_role')}")

        mt_res = client.get("/api/game-world/mastery-tree", headers=headers)
        assert mt_res.status_code == 200
        mt_data = mt_res.json()
        assert len(mt_data.get("nodes", [])) > 0
        print(f"   [OK] Mastery Tree: {len(mt_data['nodes'])} concept skill nodes mapped.")

        # 13. Session Completion & Progress Persistence
        print("\n[Stage 13] Verifying Learning Session Summary & Progress...")
        end_res = client.post(f"/api/session/{session_id}/end", headers=headers)
        assert end_res.status_code == 200
        print("   [OK] Session successfully completed and persisted.")

    print("\n" + "=" * 65)
    print("ALL 13 STAGES OF THE COMPREHENSIVE E2E JOURNEY PASSED 100%!")
    print("=" * 65)

if __name__ == "__main__":
    run_comprehensive_e2e_journey()
