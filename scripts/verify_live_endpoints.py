import os
import sys
import json
import time
from fastapi.testclient import TestClient

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.main import app

client = None
results = []

def test_endpoint(category, name, method, path, json_data=None, params=None, headers=None, expected_status=200):
    global client
    try:
        if method.upper() == "GET":
            resp = client.get(path, params=params, headers=headers)
        elif method.upper() == "POST":
            resp = client.post(path, json=json_data, params=params, headers=headers)
        elif method.upper() == "PUT":
            resp = client.put(path, json=json_data, params=params, headers=headers)
        elif method.upper() == "DELETE":
            resp = client.delete(path, params=params, headers=headers)
            
        passed = (resp.status_code == expected_status)
        results.append({
            "category": category,
            "name": name,
            "method": method.upper(),
            "path": path,
            "status": resp.status_code,
            "expected": expected_status,
            "passed": passed
        })
        status_tag = "[PASS]" if passed else f"[FAIL: {resp.status_code}]"
        print(f"{status_tag:15} | {category:16} | {method.upper():5} {path:42} | {name}")
        return resp
    except Exception as e:
        results.append({
            "category": category,
            "name": name,
            "method": method.upper(),
            "path": path,
            "status": 500,
            "expected": expected_status,
            "passed": False,
            "error": str(e)
        })
        print(f"[ERROR]         | {category:16} | {method.upper():5} {path:42} | {e}")
        return None

def run_all_tests():
    global client
    with TestClient(app) as tc:
        client = tc
        return _run_all_tests_inner()

def _run_all_tests_inner():
    print("==========================================================================================")
    print("                    NEUROQUEST LIVE ENDPOINT INTEGRATION TEST                             ")
    print("==========================================================================================")
    
    # 1. System & Health
    test_endpoint("System", "Root Health Check", "GET", "/")
    test_endpoint("System", "Health Check Alias", "GET", "/health")
    
    # 2. Authentication Flow
    unique_user = f"live_audit_{int(time.time())}"
    reg_data = {
        "username": unique_user,
        "email": f"{unique_user}@neuroquest.edu",
        "password": "Password123!",
        "role": "caregiver",
        "learner_name": "Leo Astronaut"
    }
    reg_resp = test_endpoint("Auth Engine", "Register User (/api/auth/register)", "POST", "/api/auth/register", json_data=reg_data)
    
    # Token login
    login_resp = test_endpoint("Auth Engine", "Login (/api/auth/token)", "POST", "/api/auth/token", json_data={"username": unique_user, "password": "Password123!"})
    test_endpoint("Auth Engine", "Login by Email (/api/auth/token)", "POST", "/api/auth/token", json_data={"email": f"{unique_user}@neuroquest.edu", "password": "Password123!"})
    
    auth_headers = {}
    if login_resp and login_resp.status_code == 200:
        token = login_resp.json().get("access_token")
        auth_headers = {"Authorization": f"Bearer {token}"}
        
    test_endpoint("Auth Engine", "Current User Profile (/api/auth/me)", "GET", "/api/auth/me", headers=auth_headers)
    
    # 3. Hackathon Demo Engine
    test_endpoint("Demo Engine", "Get Demo Profiles (Public)", "GET", "/api/demo/profiles")
    test_endpoint("Demo Engine", "Activate Demo Profile A", "POST", "/api/demo/activate-profile", json_data={"learner_id": "demo_learner_a"}, headers=auth_headers)
    test_endpoint("Demo Engine", "Simulate ADHD State", "POST", "/api/demo/simulate-state", json_data={"simulated_state": "ADHD (Distraction)"}, headers=auth_headers)
    test_endpoint("Demo Engine", "Simulate Autism Overload", "POST", "/api/demo/simulate-state", json_data={"simulated_state": "Autism (Sensory Overload)"}, headers=auth_headers)
    test_endpoint("Demo Engine", "Get Adaptation Explanation", "GET", "/api/demo/adaptation-explanation", headers=auth_headers)
    
    # 4. Onboarding Questionnaire
    test_endpoint("Onboarding", "Submit Caregiver Questionnaire", "POST", "/api/onboarding/questionnaire", 
                  headers=auth_headers,
                  json_data={
                      "q1_enjoyed_topics": "Rockets, Planets, Astronomy",
                      "q2_engaging_activities": "Building Lego space stations",
                      "q3_themes": ["Space"],
                      "q6_favorite_color": "blue",
                      "q12_prefer_calm_screen": True
                  })
    
    # 5. Medical Assessment (ICMR Questions)
    test_endpoint("Medical", "Get Medical Questions", "GET", "/api/medical/questions/demo_learner_a", headers=auth_headers)
    test_endpoint("Medical", "Submit Medical Profile", "POST", "/api/medical/submit", 
                  headers=auth_headers,
                  json_data={
                      "learner_id": "demo_learner_a",
                      "condition": "ADHD",
                      "answers": [{"question_id": "q1", "question_text": "Attention span", "answer": "10-15 mins"}]
                  })
    
    # 6. Learner Preferences & Personal Profile
    test_endpoint("Learner", "Get Learner Profile", "GET", "/api/learner/profile", headers=auth_headers)
    test_endpoint("Learner", "Get Specific Profile", "GET", "/api/learners/demo_learner_a/profile")
    test_endpoint("Learner", "Update Preferences", "PUT", "/api/learner/preferences", 
                  headers=auth_headers,
                  json_data={"font_family": "OpenDyslexic", "background_theme": "space"})
    
    # 7. Tasks & NCERT Curriculum
    tasks_resp = test_endpoint("Tasks Engine", "Get Tasks List", "GET", "/api/tasks", headers=auth_headers)
    task_id = "task_demo_1"
    task_question = "What is 2 + 2?"
    task_answer = "4"
    if tasks_resp and tasks_resp.status_code == 200:
        tasks_data = tasks_resp.json()
        if isinstance(tasks_data, list) and len(tasks_data) > 0:
            task_id = tasks_data[0].get("id", task_id)
            task_question = tasks_data[0].get("question", task_question)
            task_answer = tasks_data[0].get("correct_answer", task_answer)
            
    test_endpoint("Tasks Engine", "Get Task By ID", "GET", f"/api/tasks/{task_id}", headers=auth_headers)
    
    # 8. Learning Session & Telemetry
    sess_resp = test_endpoint("Session Engine", "Start Session", "POST", "/api/session/start", headers=auth_headers)
    session_id = "sess_demo_1"
    if sess_resp and sess_resp.status_code == 200:
        session_id = sess_resp.json().get("id", session_id)
        
    test_endpoint("Session Engine", "Submit Answer", "POST", f"/api/session/{session_id}/answer", 
                  headers=auth_headers,
                  json_data={
                      "task_id": task_id,
                      "selected_answer": task_answer,
                      "time_taken_seconds": 12,
                      "hints_used": 0
                  })
    test_endpoint("Session Engine", "End Session", "POST", f"/api/session/{session_id}/end", headers=auth_headers)
    
    # Telemetry ML Evaluation
    test_endpoint("Telemetry ML", "Evaluate Telemetry Flow", "POST", "/api/telemetry/evaluate", 
                  headers=auth_headers,
                  json_data={
                      "session_id": session_id,
                      "click_rate_per_min": 12.0,
                      "idle_ratio": 0.1,
                      "avg_response_time_sec": 7.5,
                      "current_difficulty": 1
                  })
    test_endpoint("Telemetry ML", "Record Interaction Event", "POST", "/api/events", 
                  headers=auth_headers,
                  json_data={"event_type": "load_check", "load_check": "Too much"})
    
    # 9. AI Agents (AI Mentor, Scaffold Ladder, Adaptive Explanation)
    test_endpoint("AI Agent", "AI Adaptive Explanation", "POST", "/api/ai/explain", 
                  headers=auth_headers,
                  json_data={
                      "question": task_question,
                      "correct_answer": task_answer,
                      "learner_interests": ["Space", "Astronomy"],
                      "guidance_level": "high"
                  })
    test_endpoint("AI Agent", "AI Gentle Hint", "POST", "/api/ai/hint", 
                  headers=auth_headers,
                  json_data={
                      "question": task_question,
                      "correct_answer": task_answer,
                      "attempt_count": 1
                  })
    test_endpoint("AI Agent", "AI Scaffold Ladder", "POST", "/api/ai/scaffold", 
                  headers=auth_headers,
                  json_data={
                      "task": {"id": task_id, "question": task_question, "correct_answer": task_answer, "subject": "Science"},
                      "attempt_count": 1
                  })
    test_endpoint("AI Agent", "Daily Welcome Mission", "GET", "/api/ai/daily-welcome", headers=auth_headers)
    test_endpoint("AI Agent", "Personalized Mission Task", "POST", "/api/ai/personalized-task", 
                  headers=auth_headers,
                  json_data={
                      "subject": "Mathematics",
                      "difficulty": 1,
                      "base_objective": "Count stellar bodies"
                  })
    
    # 10. Gamification & Mastery Tree
    test_endpoint("Gamification", "Get Personal Game World", "GET", "/api/game-world", headers=auth_headers)
    test_endpoint("Gamification", "Get Mastery Tree", "GET", "/api/game-world/mastery-tree", headers=auth_headers)
    
    # 11. Caregiver Dashboard & Progress Summary
    test_endpoint("Caregiver", "Get Caregiver Insights", "GET", "/api/caregiver/insights", headers=auth_headers)
    test_endpoint("Caregiver", "Submit Caregiver Profile", "POST", "/api/caregiver/profile", 
                  headers=auth_headers,
                  json_data={"caregiver_name": "Dr. Sarah", "learner_id": "demo_learner_a", "preferences": {"alert_threshold": "high"}})
    test_endpoint("Progress", "Get Progress Summary", "GET", "/api/progress/summary", headers=auth_headers)
    
    print("==========================================================================================")
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    failed = total - passed
    print(f"RESULTS: {passed}/{total} ENDPOINTS PASSED ({passed/total*100:.1f}%) | {failed} FAILED")
    print("==========================================================================================")
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
