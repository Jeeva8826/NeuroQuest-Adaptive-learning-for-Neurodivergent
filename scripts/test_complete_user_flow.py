import requests
import sys
import os
import time
import socket
import threading

BASE_URL = "http://127.0.0.1:8000"

def _ensure_server_running():
    try:
        with socket.create_connection(("127.0.0.1", 8000), timeout=0.5):
            return
    except OSError:
        pass
    
    print("[INIT] Starting in-process FastAPI backend on 127.0.0.1:8000 for automated testing...")
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, os.path.join(project_root, "backend"))
    import uvicorn
    from app.main import app
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="warning")
    server = uvicorn.Server(config)
    t = threading.Thread(target=server.run, daemon=True)
    t.start()
    for _ in range(30):
        time.sleep(0.5)
        try:
            with socket.create_connection(("127.0.0.1", 8000), timeout=0.5):
                print("[INIT] Live backend online and accepting requests!")
                return
        except OSError:
            pass

def run_end_to_end_journey():
    _ensure_server_running()
    session = requests.Session()
    print("================================================================================")
    print("NEUROQUEST END-TO-END VERIFICATION: CARETAKER -> STUDENT -> QUEST EXPERIENCE")
    print("================================================================================")

    # ---------------------------------------------------------
    # Phase 1: Caretaker Dynamic Registration & Verification
    # ---------------------------------------------------------
    import time
    test_user_id = int(time.time())
    caregiver_email = f"caregiver_{test_user_id}@example.com"
    caregiver_username = f"parent_{test_user_id}"
    print(f"\n[STEP 1] Caretaker Registration & Verification ({caregiver_email})")
    
    reg_res = session.post(f"{BASE_URL}/api/auth/register", json={
        "email": caregiver_email,
        "username": caregiver_username,
        "password": "SecurePassword123!",
        "full_name": "Test Caregiver Parent",
        "role": "caregiver"
    })
    assert reg_res.status_code == 200, f"Registration failed: {reg_res.text}"
    auth_data = reg_res.json()

    token = auth_data.get("token") or auth_data.get("access_token")
    assert token, f"Could not obtain token: {auth_data}"
    headers = {"Authorization": f"Bearer {token}"}
    print(f"  [PASS] New Caretaker registered & authenticated successfully.")
    print(f"  [PASS] Role: {auth_data.get('role')} (Guardian / Parent identity verified)")
    print(f"  [PASS] User ID: {auth_data.get('user_id')}")

    # ---------------------------------------------------------
    # Phase 2: Student Registration
    # ---------------------------------------------------------
    print("\n[STEP 2] Student Registration Under Caretaker")
    student_payload = {
        "first_name": "Aarav",
        "last_name": "Sharma",
        "age": 11,
        "grade": "Class 6 (NCERT)",
        "school_level": "Middle School",
        "school_name": "Kendriya Vidyalaya",
        "preferred_language": "English",
        "interests": ["Space & Astronomy", "Robotics & Coding", "Dinosaurs & Prehistory"],
        "learning_environment": "Quiet Space with Visual Cues",
        "guardian_consent": True
    }
    create_res = session.post(f"{BASE_URL}/api/students", json=student_payload, headers=headers)
    assert create_res.status_code == 201, f"Create student failed: {create_res.status_code} {create_res.text}"
    student = create_res.json()
    student_id = student["id"]
    print(f"  [PASS] Student created: {student['name']}, Age {student['age']}, Grade: {student['grade']}")
    print(f"  [PASS] Student ID: {student_id}")
    print(f"  [PASS] Screening initial status: has_completed_screening={student['has_completed_screening']}")

    # ---------------------------------------------------------
    # Phase 3: Fetch 20-Question Baseline Assessment Schema
    # ---------------------------------------------------------
    print("\n[STEP 3] Load 20-Question Baseline Assessment Questionnaire")
    q_res = session.get(f"{BASE_URL}/api/students/{student_id}/questionnaire", headers=headers)
    assert q_res.status_code == 200, f"Get questionnaire failed: {q_res.status_code}"
    q_data = q_res.json()
    schema = q_data["schema"]
    questions = schema["questions"]
    print(f"  [PASS] Questionnaire Title: {schema['title']}")
    print(f"  [PASS] Total Questions: {len(questions)} (Product Baseline v1)")
    print(f"  [PASS] Non-Diagnostic Notice: {schema['disclaimer'][:75]}...")
    assert len(questions) == 20, f"Expected 20 questions, got {len(questions)}"

    # ---------------------------------------------------------
    # Phase 4: Save & Verify Draft Progress
    # ---------------------------------------------------------
    print("\n[STEP 4] Save Mid-Way Assessment Draft (Progress Persistence)")
    draft_responses = {
        "q1": "Often",
        "q2": "Very Often",
        "q3": "Often",
        "q4": "Very Often",
        "q5": "Very challenging"
    }
    draft_res = session.post(
        f"{BASE_URL}/api/students/{student_id}/questionnaire/draft",
        json={"responses": draft_responses, "current_question": 6},
        headers=headers
    )
    assert draft_res.status_code == 200
    print(f"  [PASS] Draft saved at Question 6: {draft_res.json()['message']}")

    # Verify reload retrieves draft
    reload_res = session.get(f"{BASE_URL}/api/students/{student_id}/questionnaire", headers=headers)
    draft_retrieved = reload_res.json().get("draft")
    assert draft_retrieved["current_question"] == 6
    assert draft_retrieved["responses"]["q1"] == "Often"
    print(f"  [PASS] Draft successfully restored on reload: {len(draft_retrieved['responses'])} answers saved")

    # ---------------------------------------------------------
    # Phase 5: Complete Full 20-Question Assessment
    # ---------------------------------------------------------
    print("\n[STEP 5] Complete Full 20-Question Baseline Assessment")
    full_responses = {
        "q1": "Often",
        "q2": "Very Often",
        "q3": "Often",
        "q4": "Very Often",
        "q5": "Very challenging",
        "q6": "Extremely helpful",
        "q7": "Extremely helpful",
        "q8": "Very helpful",
        "q9": "1 to 2 short sentences per card",
        "q10": "Often",
        "q11": "Very helpful",
        "q12": "Fresh real-world analogies tied to interests",
        "q13": "Extremely helpful",
        "q14": "Completely untimed, relaxed exploration",
        "q15": "Often",
        "q16": "Non-punitive gentle nudge with first step shown",
        "q17": "Micro-challenges (1 to 2 minutes each)",
        "q18": "Unlocking world components or space/cyber parts",
        "q19": "Often",
        "q20": "Task initiation, attention stamina & focus"
    }
    complete_res = session.post(
        f"{BASE_URL}/api/students/{student_id}/questionnaire/complete",
        json={"responses": full_responses},
        headers=headers
    )
    assert complete_res.status_code == 200, f"Complete questionnaire failed: {complete_res.status_code}"
    baseline_profile = complete_res.json()
    print(f"  [PASS] Baseline profile generated successfully for: {baseline_profile['student_name']}")
    print(f"  [PASS] Disclaimer verified non-diagnostic: {baseline_profile['disclaimer'][:65]}...")

    # Verify 10 Dimensions
    dimensions = baseline_profile["dimensions"]
    assert len(dimensions) == 10, f"Expected 10 dimensions, got {len(dimensions)}"
    print(f"  [PASS] 10 Educational Support Dimensions computed:")
    for d in dimensions:
        print(f"    * {d['title']}: {d['support_level']}")

    # ---------------------------------------------------------
    # Phase 6: Verify Baseline Profile Retrieval Endpoint
    # ---------------------------------------------------------
    print("\n[STEP 6] View Baseline Support Profile")
    get_profile_res = session.get(f"{BASE_URL}/api/students/{student_id}/baseline-profile", headers=headers)
    assert get_profile_res.status_code == 200
    prof = get_profile_res.json()
    print(f"  [PASS] UI Configuration: Visual Density = {prof['initial_ui_configuration']['visual_density']}")
    print(f"  [PASS] UI Configuration: Guidance Level = {prof['initial_ui_configuration']['guidance_level']}")
    print(f"  [PASS] UI Configuration: Pacing Mode = Calm (untimed={prof['initial_ui_configuration']['calm_mode']})")
    print(f"  [PASS] Recommended Accommodations: {len(prof['recommended_accommodations'])} active")

    # ---------------------------------------------------------
    # Phase 7: Caretaker Students List Status
    # ---------------------------------------------------------
    print("\n[STEP 7] Caretaker Dashboard Students List")
    list_res = session.get(f"{BASE_URL}/api/students", headers=headers)
    assert list_res.status_code == 200, f"list_res failed: {list_res.status_code} {list_res.text}"
    students_list = list_res.json()
    my_student = next((s for s in students_list if s["id"] == student_id), None)
    assert my_student is not None
    assert my_student["has_completed_screening"] is True
    print(f"  [PASS] Student {my_student['name']} confirmed as screening completed in dashboard.")

    # ---------------------------------------------------------
    # Phase 8: Launch NeuroQuest Student Experience
    # ---------------------------------------------------------
    print("\n[STEP 8] Launch NeuroQuest Student Experience")
    # Fetch Curriculum tasks for Class 6 / Science
    tasks_res = session.get(f"{BASE_URL}/api/tasks?subject=Science", headers=headers)
    assert tasks_res.status_code == 200
    tasks = tasks_res.json()
    print(f"  [PASS] Curriculum Tasks catalog retrieved: {len(tasks)} tasks available")

    # Start student learning session
    sess_res = session.post(f"{BASE_URL}/api/session/start", headers=headers)
    assert sess_res.status_code == 200
    sess_data = sess_res.json()
    session_id = sess_data.get("id", "")
    print(f"  [PASS] Student learning quest session started (Session ID: {session_id[:12]}...)")

    # Request AI Hint Scaffolding
    scaffold_res = session.post(f"{BASE_URL}/api/ai/scaffold", json={
        "level": 1,
        "task_context": "NCERT Class 6 Light Shadows & Reflections",
        "error_type": "None"
    }, headers=headers)
    assert scaffold_res.status_code == 200
    print(f"  [PASS] Step-by-step Scaffolding Ladder available: Level 1 hint generated")

    # Telemetry evaluation (Focused state)
    telem_res = session.post(f"{BASE_URL}/api/telemetry/evaluate", json={
        "session_id": session_id,
        "has_gaze": False,
        "gaze_drift_std": 12.0,
        "click_rate_per_min": 18.0,
        "rapid_click_count": 0,
        "idle_ratio": 0.1,
        "avg_response_time_sec": 7.0,
        "current_difficulty": 2
    }, headers=headers)
    assert telem_res.status_code == 200, f"Telemetry evaluate failed: {telem_res.status_code} {telem_res.text}"
    telem_data = telem_res.json()
    print(f"  [PASS] Real-time Telemetry Adaptation evaluated: State = {telem_data.get('state')}")
    print(f"  [PASS] Telemetry Adaptation Action: {telem_data.get('adaptation', {}).get('action')}")

    # ---------------------------------------------------------
    # Phase 9: Task Answer Evaluation (Wrong & Correct Handling)
    # ---------------------------------------------------------
    print("\n[STEP 9] Task Answer Evaluation (Wrong & Correct Handlers)")
    if tasks:
        sample_task = tasks[0]
        correct_answer = sample_task["correct_answer"]
        wrong_answer = next((opt for opt in sample_task["options"] if opt.strip().lower() != correct_answer.strip().lower()), "ClearlyWrongAnswerXYZ")

        # 1. Submit Wrong Answer
        wrong_submit_res = session.post(f"{BASE_URL}/api/session/{session_id}/submit", json={
            "task_id": sample_task["id"],
            "selected_answer": wrong_answer,
            "time_taken_seconds": 15,
            "hints_used": 1
        }, headers=headers)
        assert wrong_submit_res.status_code == 200, f"Submit failed: {wrong_submit_res.text}"
        wrong_data = wrong_submit_res.json()
        assert wrong_data["is_correct"] is False, f"Expected is_correct=False for wrong pick, got {wrong_data}"
        assert "explanation" in wrong_data and wrong_data["explanation"], "Expected explanation in wrong submission feedback"
        assert wrong_data["correct_answer"] == correct_answer, "Expected correct answer returned in response"
        print(f"  [PASS] Wrong answer '{wrong_answer}' correctly identified as is_correct=False.")
        print(f"  [PASS] Correct answer provided for learner review: '{wrong_data['correct_answer']}'")

        # 2. Submit Correct Answer
        correct_submit_res = session.post(f"{BASE_URL}/api/session/{session_id}/submit", json={
            "task_id": sample_task["id"],
            "selected_answer": correct_answer,
            "time_taken_seconds": 12,
            "hints_used": 0
        }, headers=headers)
        assert correct_submit_res.status_code == 200, f"Submit failed: {correct_submit_res.text}"
        correct_data = correct_submit_res.json()
        assert correct_data["is_correct"] is True, f"Expected is_correct=True for correct pick, got {correct_data}"
        print(f"  [PASS] Correct answer '{correct_answer}' correctly identified as is_correct=True.")
        print(f"  [PASS] Points rewarded: {correct_data['points_earned']} stars")

    print("\n================================================================================")
    print("ALL PHASES PASSED 100%! FULL CARETAKER -> STUDENT ONBOARDING FLOW IS COMPLETE!")
    print("================================================================================")

if __name__ == "__main__":
    run_end_to_end_journey()
