import urllib.request
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_live():
    print("==================================================================")
    print("            NEUROQUEST LIVE HTTP CONNECTIVITY VERIFICATION        ")
    print("==================================================================")
    
    # 1. Backend direct
    try:
        with urllib.request.urlopen("http://127.0.0.1:8000/health", timeout=4) as resp:
            data = json.loads(resp.read().decode())
            print(f"[OK] Backend Direct (127.0.0.1:8000/health): Status {resp.status} - {data.get('app')}")
    except Exception as e:
        print(f"[FAIL] Backend Direct: {e}")

    # 2. Frontend direct
    try:
        with urllib.request.urlopen("http://localhost:5173/", timeout=4) as resp:
            print(f"[OK] Frontend Direct (localhost:5173): Status {resp.status} (Vite React UI Ready)")
    except Exception as e:
        print(f"[FAIL] Frontend Direct: {e}")

    # 3. Frontend to Backend Reverse Proxy
    try:
        with urllib.request.urlopen("http://localhost:5173/api/demo/profiles", timeout=4) as resp:
            data = json.loads(resp.read().decode())
            profiles = data.get("profiles", [])
            print(f"[OK] Vite Proxy (localhost:5173/api/demo/profiles): Status {resp.status} - {len(profiles)} Profiles Loaded:")
            for p in profiles:
                print(f"       -> {p['label']} ({p['interest']})")
    except Exception as e:
        print(f"[FAIL] Vite Proxy: {e}")

    print("==================================================================")

if __name__ == "__main__":
    check_live()
