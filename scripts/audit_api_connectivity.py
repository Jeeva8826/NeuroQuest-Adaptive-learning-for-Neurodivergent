import os
import sys
import re
import json

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

def find_frontend_api_calls():
    src_dir = os.path.join(os.path.dirname(__file__), "..", "frontend", "src")
    api_endpoints = []
    
    # Check api.js and api.ts specifically
    api_files = [
        os.path.join(src_dir, "services", "api.js"),
        os.path.join(src_dir, "services", "api.ts")
    ]
    
    for fpath in api_files:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                matches = re.findall(r"(?:api\.(get|post|put|delete)|fetch)\s*\(\s*[`\'\"]([^\`\'\"]+)[`\'\"]", content)
                for method, url in matches:
                    api_endpoints.append({
                        "file": os.path.basename(fpath),
                        "method": method if method else "fetch",
                        "url": url
                    })
    
    # Scan all other files in frontend/src
    for root, _, files in os.walk(src_dir):
        for fname in files:
            if fname.endswith(('.jsx', '.tsx', '.js', '.ts')) and fname not in ('api.js', 'api.ts'):
                fpath = os.path.join(root, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                    matches = re.findall(r"(?:fetch|axios\.(?:get|post|put|delete))\s*\(\s*[`\'\"]([^\`\'\"]+)[`\'\"]", content)
                    for url in matches:
                        api_endpoints.append({
                            "file": fname,
                            "method": "direct",
                            "url": url
                        })
                        
    return api_endpoints

def run_audit():
    from app.main import app
    
    frontend_calls = find_frontend_api_calls()
    backend_paths = app.openapi().get('paths', {})
    
    print("================================================================================")
    print("         NEUROQUEST FULL-STACK API CONNECTIVITY AUDIT REPORT                     ")
    print("================================================================================")
    print(f"Total Unique Backend Endpoints (OpenAPI): {len(backend_paths)}")
    print(f"Total Frontend API Invocations Audited: {len(frontend_calls)}")
    print("--------------------------------------------------------------------------------")
    
    all_matched = True
    unmatched = []
    
    for item in frontend_calls:
        src_file = item['file']
        raw_url = item['url']
        method = (item['method'] or 'ANY').upper()
        
        norm_url = raw_url
        if norm_url.startswith('http://localhost:8000'):
            norm_url = norm_url[len('http://localhost:8000'):]
        if norm_url.startswith('${API_BASE_URL}'):
            norm_url = norm_url[len('${API_BASE_URL}'):]
        if norm_url.startswith('${API}'):
            norm_url = norm_url[len('${API}'):]
        
        # If it was in api.js and didn't start with /api, api.js has baseURL: '/api'
        if src_file == 'api.js' and not norm_url.startswith('/api'):
            norm_url = '/api' + norm_url
            
        norm_url = re.sub(r'\$\{learnerId\}|\{learner_id\}', '{learner_id}', norm_url)
        norm_url = re.sub(r'\$\{taskId\}|\{task_id\}', '{task_id}', norm_url)
        norm_url = re.sub(r'\$\{sessionId\}|\{session_id\}', '{session_id}', norm_url)
        
        matched = False
        if norm_url in backend_paths:
            backend_methods = [m.upper() for m in backend_paths[norm_url].keys()]
            if method in ('ANY', 'FETCH', 'DIRECT') or method in backend_methods:
                matched = True
                
        if matched:
            print(f"[OK] MATCHED: [{src_file:15}] {method:6} {raw_url:42} -> Backend: {norm_url}")
        else:
            all_matched = False
            unmatched.append((src_file, method, raw_url, norm_url))
            print(f"[FAIL] MISMATCH: [{src_file:15}] {method:6} {raw_url:42} -> Target: {norm_url}")
            
    print("================================================================================")
    if all_matched:
        print("[SUCCESS] 100% of frontend API calls are properly connected to backend endpoints!")
    else:
        print(f"[WARNING] {len(unmatched)} endpoints had mismatches.")
        
    return all_matched

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
