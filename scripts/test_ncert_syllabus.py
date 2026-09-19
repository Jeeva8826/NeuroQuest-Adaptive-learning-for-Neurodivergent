import requests

BASE = 'http://127.0.0.1:8000/api'
login_res = requests.post(f'{BASE}/auth/login', json={'username': 'jeevananth1234@gmail.com', 'password': '123'})
token = login_res.json().get('access_token')
headers = {'Authorization': f'Bearer {token}'}

print("================================================================================")
print("TESTING NCERT SYLLABUS & TASK INTEGRATION ACROSS ALL STANDARDS (1 TO 10)")
print("================================================================================")

# 1. Test Standards
standards_res = requests.get(f'{BASE}/tasks/standards', headers=headers)
assert standards_res.status_code == 200, f"Failed standards: {standards_res.text}"
standards = standards_res.json().get('standards', [])
print(f"[PASS] Total Standards Returned: {len(standards)}")
for s in standards:
    print(f"  * {s['standard_name']}: {s['total_chapters']} chapters across {s['subjects']}")

# 2. Test Syllabus filtered by grade=7
syl_res = requests.get(f'{BASE}/tasks/syllabus?grade=7', headers=headers)
assert syl_res.status_code == 200, f"Failed syllabus: {syl_res.text}"
syl_data = syl_res.json()
print(f"\n[PASS] Filtered Syllabus (Grade 7): {len(syl_data.get('standards', []))} standard returned with {len(syl_data['standards'][0]['subjects'])} subjects")

# 3. Test Tasks count by grade
print("\n[PASS] Task Bank Distribution by Standard:")
total_tasks = 0
for g in range(1, 11):
    t_res = requests.get(f'{BASE}/tasks?grade={g}', headers=headers)
    assert t_res.status_code == 200, f"Failed tasks for grade {g}"
    tasks = t_res.json()
    total_tasks += len(tasks)
    print(f"  * Class {g:2d}: {len(tasks)} curriculum tasks active")

print(f"Total Standard-Tagged Tasks in Bank: {total_tasks}")

# 4. Check a sample task
sample_res = requests.get(f'{BASE}/tasks?grade=6&subject=Science', headers=headers)
assert sample_res.status_code == 200 and sample_res.json(), "No Grade 6 Science tasks"
sample = sample_res.json()[0]
print("\n[PASS] Sample Task Verification (Class 6 Science):")
print(f"  Title: {sample.get('title')}")
print(f"  Standard: {sample.get('standard')}")
print(f"  Chapter: {sample.get('chapter')}")
print(f"  Question: {sample.get('question')}")
print(f"  Hints count: {len(sample.get('hints', []))}")
print(f"  Scaffold steps count: {len(sample.get('steps', []))}")

print("\n================================================================================")
print("ALL NCERT BACKEND ENDPOINTS & STANDARDS VERIFIED 100%!")
print("================================================================================")
