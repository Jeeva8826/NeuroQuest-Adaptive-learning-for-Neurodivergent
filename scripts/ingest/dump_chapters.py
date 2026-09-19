import json

with open("data/curriculum/ncert_master_syllabus.json", encoding="utf-8") as f:
    d = json.load(f)

for s in d["standards"][:5]:
    print(f"=== {s['standard_name']} ===")
    for sub in s["subjects"]:
        for ch in sub["chapters"]:
            print(f"{s['grade']}|{sub['subject']}|{ch['chapter_number']}|{ch['title']}|{','.join(ch.get('topics', []))}")
