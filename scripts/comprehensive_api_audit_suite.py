import sys
import json
import time
import uuid
import urllib.request
import urllib.error
from typing import Dict, Any, Tuple

import os
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

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

results = {
    "total_tested": 0,
    "pass": 0,
    "fail": 0,
    "blocked": 0,
    "endpoints": []
}

def record_test(method: str, endpoint: str, purpose: str, passed: bool, status_code: int, error_msg: str = "", caller: str = "Frontend/Axios"):
    results["total_tested"] += 1
    if passed:
        results["pass"] += 1
        res_str = f"{GREEN}PASS{RESET}"
    else:
        results["fail"] += 1
        res_str = f"{RED}FAIL{RESET}"
        
    print(f"[{res_str}] {method:6} {endpoint:42} (HTTP {status_code}) - {purpose}")
    if error_msg:
        print(f"       {RED}Error: {error_msg}{RESET}")
        
    results["endpoints"].append({
        "method": method,
        "endpoint": endpoint,
        "purpose": purpose,
        "status": "PASS" if passed else "FAIL",
        "http_code": status_code,
        "caller": caller,
        "error": error_msg
    })

def make_request(method: str, path: str, data: Dict[str, Any] = None, token: str = None) -> Tuple[int, Dict[str, Any], str]:
    url = f"{BASE_URL}{path}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    req_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            code = res.status
            body_text = res.read().decode("utf-8")
            try:
                body_json = json.loads(body_text)
            except Exception:
                body_json = {"raw": body_text}
            return code, body_json, ""
    except urllib.error.HTTPError as e:
        code = e.code
        body_text = e.read().decode("utf-8")
        try:
            body_json = json.loads(body_text)
        except Exception:
            body_json = {"raw": body_text}
        return code, body_json, e.reason
    except Exception as e:
        return 0, {}, str(e)

def run_audit():
    _ensure_server_running()
    print("=" * 80)
    print("NEUROQUEST FULL SPECTRUM API & BACKEND INTEGRATION AUDIT SUITE")
    print("=" * 80)
    
    # ----------------------------------------------------
    # PHASE 1: Health & Startup APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Health & Server Initialization Endpoints ---{RESET}")
    for p in ["/", "/health", "/api/health"]:
        code, body, err = make_request("GET", p)
        passed = (code == 200 and ("status" in body or "app" in body or "online" in str(body)))
        record_test("GET", p, "Service Health & Metadata Check", passed, code, err, "System/Browser")
        
    # ----------------------------------------------------
    # PHASE 2: Authentication APIs (Full Lifecycle & Security)
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Authentication & Token Handshake ---{RESET}")
    unique_suffix = str(int(time.time()))[-6:]
    test_user = f"audit_user_{unique_suffix}"
    test_email = f"audit_{unique_suffix}@example.com"
    test_pwd = "AuditPassword123!"
    
    # 1. Register User (/auth/register)
    reg_payload = {
        "username": test_user,
        "email": test_email,
        "password": test_pwd,
        "full_name": "QA Auditor Caregiver",
        "role": "CAREGIVER"
    }
    code, body, err = make_request("POST", "/auth/register", reg_payload)
    passed = (code == 200 and "access_token" in body)
    token = body.get("access_token", "")
    record_test("POST", "/auth/register", "Caregiver Registration (Dual DB & Token Issue)", passed, code, err, "RegisterPage.jsx")
    
    # 2. Duplicate Registration Rejection (Security & Validation)
    code, body, err = make_request("POST", "/auth/register", reg_payload)
    passed = (code == 400)
    record_test("POST", "/auth/register", "Duplicate User Registration Rejection (HTTP 400)", passed, code, err, "RegisterPage.jsx")

    # 3. /api/auth/register alias endpoint
    alias_user = f"alias_{unique_suffix}"
    code, body, err = make_request("POST", "/api/auth/register", {
        "username": alias_user,
        "email": f"{alias_user}@test.com",
        "password": test_pwd,
        "full_name": "Alias User",
        "role": "CAREGIVER"
    })
    passed = (code == 200 and "access_token" in body)
    record_test("POST", "/api/auth/register", "API Prefix Registration Endpoint", passed, code, err, "api.js")

    # 4. Login via /auth/token (Username)
    code, body, err = make_request("POST", "/auth/token", {"username": test_user, "password": test_pwd})
    passed = (code == 200 and "access_token" in body)
    token = body.get("access_token", token)
    record_test("POST", "/auth/token", "User Login by Username (JWT Issuance)", passed, code, err, "LoginPage.jsx")

    # 5. Login via /auth/token (Email)
    code, body, err = make_request("POST", "/auth/token", {"username": test_email, "password": test_pwd})
    passed = (code == 200 and "access_token" in body)
    record_test("POST", "/auth/token", "User Login by Email (Case-Insensitive Resolution)", passed, code, err, "LoginPage.jsx")

    # 6. Login via /api/auth/token alias
    code, body, err = make_request("POST", "/api/auth/token", {"username": test_user, "password": test_pwd})
    passed = (code == 200 and "access_token" in body)
    record_test("POST", "/api/auth/token", "API Prefix Login Endpoint", passed, code, err, "api.js")

    # 7. Invalid Credentials Rejection (Security)
    code, body, err = make_request("POST", "/auth/token", {"username": test_user, "password": "WrongPassword!"})
    passed = (code == 401)
    record_test("POST", "/auth/token", "Invalid Password Rejection (HTTP 401)", passed, code, err, "LoginPage.jsx")

    # 8. Token Authentication: /auth/whoami
    code, body, err = make_request("GET", "/auth/whoami", token=token)
    passed = (code == 200 and body.get("username") == test_user)
    record_test("GET", "/auth/whoami", "Token Verification & User Profile Retrieval", passed, code, err, "AuthContext.jsx")

    # 9. Token Authentication: /api/auth/me
    code, body, err = make_request("GET", "/api/auth/me", token=token)
    passed = (code == 200 and body.get("username") == test_user)
    learner_id = body.get("learner_id", "")
    record_test("GET", "/api/auth/me", "Current Authenticated User Identity Endpoint", passed, code, err, "api.js")

    # 10. Unauthenticated Access Rejection (Security)
    code, body, err = make_request("GET", "/api/auth/me", token=None)
    passed = (code == 401)
    record_test("GET", "/api/auth/me", "Unauthenticated Request Rejection (HTTP 401)", passed, code, err, "ProtectedRoute.jsx")

    # 11. Malformed Token Rejection (Security)
    code, body, err = make_request("GET", "/api/auth/me", token="INVALID_TAMPERED_JWT_HEADER_PAYLOAD_SIGNATURE")
    passed = (code == 401)
    record_test("GET", "/api/auth/me", "Tampered/Malformed JWT Rejection (HTTP 401)", passed, code, err, "Axios Interceptor")

    # ----------------------------------------------------
    # PHASE 3: Onboarding & Caregiver Profile APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Onboarding, Caregiver & Preferences Endpoints ---{RESET}")
    # Submit 20-Question Non-Diagnostic Caregiver Assessment
    q_payload = {
        "q1_learning_environment": "Quiet, distraction-minimized space",
        "q2_content_format": "Visual diagrams, charts & infographics",
        "q3_text_tolerance": "Bite-sized sentences (1 to 2 lines per card)",
        "q4_visual_support": "High visual support (diagrams, color coding, icons)",
        "q5_audio_support": "On-demand audio button (listen when helpful)",
        "q6_pace_preference": "Completely untimed, relaxed exploration",
        "q7_response_time": "Needs extended time to think before answering",
        "q8_distraction_sensitivity": "High — visual motion or moving elements break focus",
        "q9_content_density": "Single-concept focus (one idea and one action per screen)",
        "q10_task_chunking": "Micro-challenges (1 to 2 minutes each)",
        "q11_repetition_preference": "Spiral review (concept revisited with new fresh analogies)",
        "q12_instruction_complexity": "Single-clause direct instructions",
        "q13_difficulty_tolerance": "Prefers high early success with very gradual challenge ramps",
        "q14_frustration_recovery": "Offer a 1-minute calming sensory break or breathing visual",
        "q15_example_preference": "Real-world analogy tied to child's special interest",
        "q16_step_guidance": "Always scaffolded (break every question into mini-steps)",
        "q17_break_frequency": "Every 5 to 7 minutes with calm sensory animations",
        "q18_reinforcement_style": "Visual unlocks (opening new planets, sanctuaries, or cyber parts)",
        "q19_communication_style": "Visual choice cards and one-click confirmations",
        "q20_accommodations": ["Visual timers", "High contrast mode", "Audio reader"]
    }
    code, body, err = make_request("POST", "/api/onboarding/questionnaire", q_payload, token=token)
    passed = (code == 200 and "visual_preferences" in body)
    if passed and not learner_id:
        learner_id = body.get("learner_id", "")
    record_test("POST", "/api/onboarding/questionnaire", "Submit 20-Q Caregiver Onboarding Assessment", passed, code, err, "StepWizard.jsx")

    # Get Caregiver Questionnaire Schema
    code, body, err = make_request("GET", "/api/caregiver/questionnaire", token=token)
    passed = (code == 200 and ("questions" in body or "sections" in body))
    record_test("GET", "/api/caregiver/questionnaire", "Fetch Caregiver Questionnaire Schema", passed, code, err, "api.js")

    # Get Caregiver Insights
    code, body, err = make_request("GET", "/api/caregiver/insights", token=token)
    passed = (code == 200 and "learner_name" in body)
    record_test("GET", "/api/caregiver/insights", "Fetch Caregiver Dashboard Insights & Metrics", passed, code, err, "CaregiverDashboardPage.jsx")

    # ----------------------------------------------------
    # PHASE 4: Learner Profile & Preferences APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Learner Profile & Theme Preferences ---{RESET}")
    # Get Learner Profile
    code, body, err = make_request("GET", "/api/learner/profile", token=token)
    passed = (code == 200 and "visual_preferences" in body)
    record_test("GET", "/api/learner/profile", "Retrieve Authenticated Learner Profile", passed, code, err, "ThemeContext.jsx")

    # Update Learner Preferences
    pref_update = {
        "primary_color": "#10b981",
        "palette_type": "soft",
        "background_theme": "space",
        "font_family": "sans",
        "font_scale": "large",
        "visual_density": "spacious",
        "sound_enabled": False
    }
    code, body, err = make_request("PUT", "/api/learner/preferences", pref_update, token=token)
    passed = (code == 200 and ("status" in body or "visual_preferences" in body or "learner_id" in body))
    record_test("PUT", "/api/learner/preferences", "Update Learner Accessibility & Theme Preferences", passed, code, err, "SettingsPage.jsx")

    # ----------------------------------------------------
    # PHASE 5: Curriculum & Task APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing NCERT Curriculum & Tasks APIs ---{RESET}")
    # Get All Tasks
    code, body, err = make_request("GET", "/api/tasks", token=token)
    tasks = body if isinstance(body, list) else []
    passed = (code == 200 and len(tasks) > 0)
    task_id = tasks[0]["id"] if tasks else "SCI_CH01_TASK01"
    task_obj = tasks[0] if tasks else {"correct_answer": "Oxygen"}
    record_test("GET", "/api/tasks", f"Fetch Curriculum Tasks Catalog ({len(tasks)} tasks loaded)", passed, code, err, "LearnerHomePage.jsx")

    # Filter Tasks by Subject & Difficulty
    code, body, err = make_request("GET", "/api/tasks?subject=Science&difficulty=1", token=token)
    passed = (code == 200 and isinstance(body, list))
    record_test("GET", "/api/tasks?subject=Science&difficulty=1", "Filter Tasks by Subject & Level", passed, code, err, "api.js")

    # Get Single Task by ID
    code, body, err = make_request("GET", f"/api/tasks/{task_id}", token=token)
    passed = (code == 200 and body.get("id") == task_id)
    record_test("GET", f"/api/tasks/{task_id}", "Fetch Task Details by Unique ID", passed, code, err, "SessionPage.jsx")

    # Get Non-Existent Task (404 Verification)
    code, body, err = make_request("GET", "/api/tasks/NON_EXISTENT_TASK_9999", token=token)
    passed = (code == 404)
    record_test("GET", "/api/tasks/NON_EXISTENT_TASK_9999", "Query Invalid Task ID (HTTP 404)", passed, code, err, "SessionPage.jsx")

    # ----------------------------------------------------
    # PHASE 6: Learning Session & Scaffolding APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Session Lifecycle & 7-Level Scaffolding ---{RESET}")
    # Start Session
    code, body, err = make_request("POST", "/api/session/start", token=token)
    passed = (code == 200 and "id" in body)
    session_id = body.get("id", "")
    record_test("POST", "/api/session/start", f"Initialize Learning Session (Session ID: {session_id[:8]}...)", passed, code, err, "SessionPage.jsx")

    # AI Daily Welcome Mission
    code, body, err = make_request("GET", "/api/ai/daily-welcome", token=token)
    passed = (code == 200 and ("welcome_title" in body or "mission_title" in body or "greeting" in body))
    record_test("GET", "/api/ai/daily-welcome", "Generate AI Personalized Daily Welcome Mission", passed, code, err, "LearnerHomePage.jsx")

    # AI Personalized Task Generator
    code, body, err = make_request("POST", "/api/ai/personalized-task", {
        "subject": "Science",
        "difficulty": 1,
        "concept_focus": "Photosynthesis"
    }, token=token)
    passed = (code == 200 and ("task" in body or "question" in body or "title" in body))
    record_test("POST", "/api/ai/personalized-task", "Generate AI Contextual Task via Agent Engine", passed, code, err, "ai_mentor.py")

    # Test Grounded 6-Level Scaffolding Architecture (Levels 0 to 5) & Legacy Compatibility (6 to 7)
    for lvl in range(0, 8):
        scaffold_payload = {
            "task_id": task_id,
            "session_id": session_id,
            "failed_attempts": lvl,
            "hint_level": lvl
        }
        code, body, err = make_request("POST", "/api/ai/scaffold", scaffold_payload, token=token)
        passed = (code == 200 and "scaffold_level" in body and body.get("scaffold_level") == lvl)
        record_test("POST", "/api/ai/scaffold", f"Scaffolding Ladder Level {lvl} Generation", passed, code, err, "ScaffoldedHintBox.jsx")

    # Submit Incorrect Answer (Check non-punitive guidance)
    code, body, err = make_request("POST", f"/api/session/{session_id}/answer", {
        "task_id": task_id,
        "selected_answer": "INCORRECT_PROBE_OPTION_VALUE_9999",
        "response_time_ms": 4500
    }, token=token)
    passed = (code == 200 and body.get("is_correct") is False and "feedback_message" in body)
    record_test("POST", f"/api/session/{session_id}/answer", "Submit Incorrect Answer (Triggers Non-Punitive Feedback)", passed, code, err, "SessionPage.jsx")

    # Submit Correct Answer (Check mastery reward)
    code, body, err = make_request("POST", f"/api/session/{session_id}/answer", {
        "task_id": task_id,
        "selected_answer": task_obj.get("correct_answer", "Oxygen"),
        "response_time_ms": 3200
    }, token=token)
    passed = (code == 200 and body.get("is_correct") is True and body.get("points_earned", 0) > 0)
    record_test("POST", f"/api/session/{session_id}/answer", "Submit Correct Answer (Points & Mastery Progression)", passed, code, err, "SessionPage.jsx")

    # AI Adaptive Explanation (RAG & Socratic tutor)
    code, body, err = make_request("POST", "/api/ai/explain", {
        "question": "Why do leaves look green?",
        "correct_answer": "Chlorophyll absorbs red and blue light and reflects green light."
    }, token=token)
    passed = (code == 200 and "explanation" in body)
    record_test("POST", "/api/ai/explain", "RAG-Grounded AI Adaptive Explanation", passed, code, err, "ai_assist.py")

    # End Session
    code, body, err = make_request("POST", f"/api/session/{session_id}/end", token=token)
    passed = (code == 200 and "status" in body)
    record_test("POST", f"/api/session/{session_id}/end", "Conclude Learning Session & Persist Summary", passed, code, err, "SessionPage.jsx")

    # ----------------------------------------------------
    # PHASE 7: Telemetry & ML Adaptation Engine APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Telemetry & Real-Time Adaptation Engine ---{RESET}")
    # 1. Telemetry Evaluation: Focused State
    code, body, err = make_request("POST", "/api/telemetry/evaluate", {
        "session_id": session_id,
        "has_gaze": False,
        "gaze_drift_std": 12.0,
        "click_rate_per_min": 18.0,
        "rapid_click_count": 0,
        "idle_ratio": 0.1,
        "avg_response_time_sec": 7.0,
        "current_difficulty": 2
    }, token=token)
    passed = (code == 200 and "state" in body and "adaptation" in body)
    record_test("POST", "/api/telemetry/evaluate", "Telemetry Evaluation: Focused State Inference", passed, code, err, "telemetryService.js")

    # 2. Telemetry Evaluation: Possible Fatigue State (Triggers Calm Mode)
    code, body, err = make_request("POST", "/api/telemetry/evaluate", {
        "session_id": session_id,
        "has_gaze": False,
        "gaze_drift_std": 65.0,
        "click_rate_per_min": 5.0,
        "rapid_click_count": 3,
        "idle_ratio": 0.6,
        "avg_response_time_sec": 28.0,
        "current_difficulty": 2
    }, token=token)
    passed = (code == 200 and ("adaptation" in body or "state" in body))
    record_test("POST", "/api/telemetry/evaluate", "Telemetry Evaluation: Cognitive Fatigue Adaptation Trigger", passed, code, err, "telemetryService.js")

    # 3. General Events Record (/api/events)
    code, body, err = make_request("POST", "/api/events", {"event_type": "load_check", "load_check": "Too much"})
    passed = (code == 200 and body.get("adapted") is True)
    record_test("POST", "/api/events", "Record General Interaction Event & Sensory Load Adaptation", passed, code, err, "api.ts")

    # 4. Async Event Record (/auth/events/async)
    code, body, err = make_request("POST", "/auth/events/async", {
        "event_type": "nav_click",
        "path": "/home"
    }, token=token)
    passed = (code == 200 and ("status" in body or "message" in body))
    record_test("POST", "/auth/events/async", "Record Asynchronous Interaction Telemetry Event", passed, code, err, "Navbar.jsx")

    # ----------------------------------------------------
    # PHASE 8: Gamification & Progress APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Gamification, Game World & Progress ---{RESET}")
    # Personal Game World
    code, body, err = make_request("GET", "/api/game-world", token=token)
    passed = (code == 200 and "world_name" in body)
    record_test("GET", "/api/game-world", "Fetch Personal Game World & Thematic Sanctuary", passed, code, err, "LearnerHomePage.jsx")

    # Personal Mastery Tree
    code, body, err = make_request("GET", "/api/game-world/mastery-tree", token=token)
    passed = (code == 200 and "nodes" in body)
    record_test("GET", "/api/game-world/mastery-tree", "Fetch Non-Competitive Mastery Tree (Skill Graph)", passed, code, err, "ProgressPage.jsx")

    # Progress Summary
    code, body, err = make_request("GET", "/api/progress/summary", token=token)
    passed = (code == 200 and "total_stars" in body)
    record_test("GET", "/api/progress/summary", "Retrieve Cumulative Mastery Stars & Progress", passed, code, err, "ProgressPage.jsx")

    # ----------------------------------------------------
    # PHASE 9: Medical & ICMR Assessment Proxy APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Medical & ICMR Assessment Proxy APIs ---{RESET}")
    code, body, err = make_request("GET", f"/api/medical/questions/{learner_id or 'learner_1'}", token=token)
    passed = (code == 200 and isinstance(body, list) and len(body) > 0)
    record_test("GET", f"/api/medical/questions/{learner_id or 'learner_1'}", "Fetch ICMR Pediatric Questions", passed, code, err, "MedicalOnboardingPage.jsx")

    code, body, err = make_request("POST", "/api/medical/submit", {
        "learner_id": learner_id or "learner_1",
        "condition": "ADHD Support Profile",
        "answers": [{"question_id": "ICMR-1", "question_text": "Sample", "answer": "Sometimes"}]
    }, token=token)
    passed = (code == 200 and body.get("status") == "success")
    record_test("POST", "/api/medical/submit", "Submit Medical Support Profile Responses", passed, code, err, "MedicalOnboardingPage.jsx")

    # ----------------------------------------------------
    # PHASE 10: Hackathon Demo Simulation APIs
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Hackathon Demo Simulation Mode ---{RESET}")
    # Get Demo Profiles
    code, body, err = make_request("GET", "/api/demo/profiles")
    passed = (code == 200 and ("profiles" in body or isinstance(body, list)))
    record_test("GET", "/api/demo/profiles", "Fetch Pre-Configured Demo Persona Profiles (Leo, Maya, Kai)", passed, code, err, "HackathonDemoBar.jsx")

    # Activate Demo Profile
    code, body, err = make_request("POST", "/api/demo/activate-profile", {"learner_id": "demo_learner_a"}, token=token)
    passed = (code == 200 and (body.get("status") == "success" or body.get("status") == "active"))
    record_test("POST", "/api/demo/activate-profile", "Instantly Activate Demo Profile (Judge Demonstration)", passed, code, err, "HackathonDemoBar.jsx")

    # Simulate Cognitive State
    code, body, err = make_request("POST", "/api/demo/simulate-state", {"simulated_state": "POSSIBLE_FATIGUE"}, token=token)
    passed = (code == 200 and ("adaptation" in body or body.get("simulated_state") == "POSSIBLE_FATIGUE"))
    record_test("POST", "/api/demo/simulate-state", "Simulate Live Cognitive State & Force UI Adaptation", passed, code, err, "HackathonDemoBar.jsx")

    # Adaptation Explanation (Transparent & Reversible)
    code, body, err = make_request("GET", "/api/demo/adaptation-explanation", token=token)
    passed = (code == 200 and ("title" in body or "ui_mode" in body or "adaptation_reasons" in body or "what_changed" in body))
    record_test("GET", "/api/demo/adaptation-explanation", "Retrieve Transparent Adaptation Explainer Data", passed, code, err, "AdaptationExplainer.jsx")

    # ----------------------------------------------------
    # PHASE 11: Security & Boundary Verification
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing Security, Boundary & Injection Resilience ---{RESET}")
    # 1. SQL / NoSQL Injection payload in auth field
    code, body, err = make_request("POST", "/auth/token", {
        "username": "' OR '1'='1",
        "password": "' OR '1'='1"
    })
    passed = (code == 401 and "token" not in body)
    record_test("POST", "/auth/token", "SQL Injection Protection on Auth Handshake", passed, code, err, "Security Probe")

    # 2. XSS Script Injection payload in telemetry payload
    code, body, err = make_request("POST", "/api/telemetry/evaluate", {
        "session_id": "<script>alert('XSS')</script>",
        "current_difficulty": 2
    }, token=token)
    passed = (code in [200, 400, 422] and "<script>" not in str(body))
    record_test("POST", "/api/telemetry/evaluate", "XSS Payload Neutralization in Telemetry", passed, code, err, "Security Probe")

    # 3. Malformed JSON / Field Type Mismatch (Pydantic 422 Validation)
    code, body, err = make_request("POST", "/api/telemetry/evaluate", {
        "session_id": 12345, # should be string
        "gaze_drift_std": "NOT_A_FLOAT"
    }, token=token)
    passed = (code == 422)
    record_test("POST", "/api/telemetry/evaluate", "Malformed Payload Type Validation (HTTP 422)", passed, code, err, "Pydantic Validator")

    # ----------------------------------------------------
    # PHASE 12: NCERT PGVector RAG & Student Answer Evaluator
    # ----------------------------------------------------
    print(f"\n{CYAN}--- Testing NCERT PGVector RAG & Pedagogical Answer Evaluator ---{RESET}")
    # 1. RAG Pipeline Status
    code, body, err = make_request("GET", "/api/rag/status")
    passed = (code == 200 and "pipeline" in body and body.get("status") == "operational")
    record_test("GET", "/api/rag/status", "NCERT PGVector RAG Pipeline Status Probe", passed, code, err, "rag.py")

    # 2. RAG Hybrid Search
    code, body, err = make_request("POST", "/api/rag/search", {
        "query": "photosynthesis autotrophic plants",
        "grade": 7,
        "subject": "Science",
        "top_k": 3
    })
    passed = (code == 200 and len(body.get("results", [])) > 0 and "score" in body["results"][0])
    record_test("POST", "/api/rag/search", "Grounded NCERT Hybrid Search (Vector + Lexical)", passed, code, err, "rag.py")

    # 3. Grounded RAG Question Answering
    code, body, err = make_request("POST", "/api/rag/ask", {
        "question": "What is photosynthesis and how do green plants make food?",
        "grade": 7,
        "subject": "Science",
        "learner_interests": ["space"]
    })
    passed = (code == 200 and body.get("grounded") is True and len(body.get("citations", [])) > 0)
    record_test("POST", "/api/rag/ask", "NCERT Grounded Q&A with Evidence Citations", passed, code, err, "rag.py")

    # 4. Contextual AI Assistant (6-Level Scaffolding Grounding)
    code, body, err = make_request("POST", "/api/ai/contextual-assist", {
        "user_message": "Can you give me a clue about photosynthesis without giving away the answer?",
        "task": {
            "question": "What gas do plants release during photosynthesis?",
            "correct_answer": "Oxygen",
            "concept_name": "Photosynthesis"
        },
        "scaffold_level": 1,
        "learner_interests": ["space"]
    })
    passed = (code == 200 and "assistant_reply" in body and body.get("scaffold_level") == 1)
    record_test("POST", "/api/ai/contextual-assist", "Contextual AI Assistant with Level-1 Hint Protection", passed, code, err, "ai_assist.py")

    # 5. Student Answer Evaluator Endpoint
    code, body, err = make_request("POST", "/api/ai/evaluate-answer", {
        "question": "What gas do green plants release during photosynthesis?",
        "student_answer": "Oxygen",
        "correct_answer": "Oxygen",
        "learner_interests": ["space"]
    })
    passed = (code == 200 and body.get("status") == "CORRECT" and "feedback" in body and "next_step" in body)
    record_test("POST", "/api/ai/evaluate-answer", "Structured Student Answer Evaluator (Correct)", passed, code, err, "student_answer_evaluator.py")

    # 6. Student Answer Evaluator Misconception / Divergent Detection
    code, body, err = make_request("POST", "/api/ai/evaluate-answer", {
        "question": "Are plants autotrophs or heterotrophs?",
        "student_answer": "Plants are only theoretical with no real-world application",
        "correct_answer": "Autotrophs",
        "concept_id": "CON_MAT_G1_01"
    })
    passed = (code == 200 and "reason" in body and "correct_concept" in body)
    record_test("POST", "/api/ai/evaluate-answer", "Structured Student Answer Evaluator (Misconception/Divergence)", passed, code, err, "student_answer_evaluator.py")

    # ----------------------------------------------------
    # SUMMARY REPORT
    # ----------------------------------------------------
    print("\n" + "=" * 80)
    print("AUDIT EXECUTION SUMMARY")
    print("=" * 80)
    print(f"Total API Endpoints / Scenarios Tested: {results['total_tested']}")
    print(f"Passed: {GREEN}{results['pass']}{RESET}")
    print(f"Failed: {RED}{results['fail']}{RESET}")
    print(f"Pass Rate: {GREEN if results['fail'] == 0 else RED}{results['pass'] / results['total_tested'] * 100:.1f}%{RESET}")
    print("=" * 80)
    
    # Save test results JSON
    with open("docs/api_audit_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("Results saved to docs/api_audit_results.json")

    return results["fail"] == 0

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
