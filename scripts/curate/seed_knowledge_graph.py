import os
import sys
import json
import asyncio
from datetime import datetime

# Enable UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
from app.database import connect_to_mongo, get_database, engine, Base, SessionLocal
from app.models.schema import Subject, Chapter, Concept, LearningObjective, Question, QuestionVariant

async def seed_knowledge_graph():
    kg_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "curriculum", "ncert_knowledge_graph.json")
    if not os.path.exists(kg_path):
        print(f"[ERROR] Knowledge graph file not found at: {kg_path}")
        return

    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    print("==========================================================================")
    print(f"      SEEDING NCERT STRUCTURED KNOWLEDGE GRAPH (Board: {kg.get('board')})  ")
    print("==========================================================================")

    # 1. Connect and seed MongoDB
    await connect_to_mongo()
    db = get_database()

    total_concepts = 0
    total_questions = 0

    for sub in kg.get("subjects", []):
        sub_name = sub.get("subject_name")
        grade = sub.get("grade", 7)
        print(f"\n[SUBJECT] {sub_name} (Grade {grade})")

        for ch in sub.get("chapters", []):
            ch_num = ch.get("chapter_number")
            ch_title = ch.get("title")
            print(f"  └── [CHAPTER {ch_num}] {ch_title}")

            for top in ch.get("topics", []):
                top_title = top.get("title")
                print(f"       └── [TOPIC] {top_title}")

                for con in top.get("concepts", []):
                    c_id = con.get("concept_id")
                    c_name = con.get("concept_name")
                    total_concepts += 1
                    print(f"            ├── [CONCEPT] ({c_id}) {c_name}")

                    # Upsert concept into MongoDB
                    con_doc = {
                        "concept_id": c_id,
                        "subject": sub_name,
                        "grade": grade,
                        "chapter": ch_title,
                        "topic": top_title,
                        "name": c_name,
                        "difficulty": con.get("difficulty", 1.0),
                        "learning_objectives": con.get("learning_objectives", []),
                        "prerequisites": con.get("prerequisites", []),
                        "explanation": con.get("explanation", {}),
                        "concrete_examples": con.get("concrete_examples", []),
                        "misconceptions": con.get("common_misconceptions", []),
                        "updated_at": datetime.utcnow()
                    }
                    await db["concepts"].update_one({"concept_id": c_id}, {"$set": con_doc}, upsert=True)

                    # Extract and upsert questions as LearningTasks
                    for q in con.get("questions", []):
                        total_questions += 1
                        q_id = q.get("question_id")
                        task_doc = {
                            "id": q_id,
                            "concept_id": c_id,
                            "subject": sub_name,
                            "grade": grade,
                            "chapter": ch_title,
                            "title": f"{c_name} — Level {q.get('difficulty', 1)}",
                            "cognitive_level": q.get("cognitive_level", "RECALL"),
                            "difficulty": q.get("difficulty", 1),
                            "question": q.get("prompt"),
                            "options": q.get("options", []),
                            "correct_answer": q.get("correct_answer"),
                            "explanation": q.get("explanation"),
                            "hints": q.get("hints", []),
                            "scaffold_steps": q.get("scaffold_steps", []),
                            "prerequisites": con.get("prerequisites", []),
                            "board": "NCERT",
                            "updated_at": datetime.utcnow()
                        }
                        await db["tasks"].update_one({"id": q_id}, {"$set": task_doc}, upsert=True)
                        print(f"            │    └── [QUESTION] ({q_id}) {q.get('cognitive_level')} (Diff: {q.get('difficulty')})")

    print("--------------------------------------------------------------------------")
    print(f"[OK] Successfully Seeded MongoDB: {total_concepts} Concepts, {total_questions} Structured Questions.")

    # 2. Seed relational PostgreSQL if accessible
    if engine is not None:
        try:
            Base.metadata.create_all(bind=engine)
            pg_session = SessionLocal()

            for sub in kg.get("subjects", []):
                sub_obj = pg_session.query(Subject).filter_by(name=sub.get("subject_name")).first()
                if not sub_obj:
                    sub_obj = Subject(name=sub.get("subject_name"), description=f"NCERT Grade {sub.get('grade')} {sub.get('subject_name')}")
                    pg_session.add(sub_obj)
                    pg_session.commit()
                    pg_session.refresh(sub_obj)

                for ch in sub.get("chapters", []):
                    ch_obj = pg_session.query(Chapter).filter_by(subject_id=sub_obj.id, title=ch.get("title")).first()
                    if not ch_obj:
                        ch_obj = Chapter(subject_id=sub_obj.id, title=ch.get("title"), order_index=ch.get("chapter_number", 1))
                        pg_session.add(ch_obj)
                        pg_session.commit()
                        pg_session.refresh(ch_obj)

                    for top in ch.get("topics", []):
                        for con in top.get("concepts", []):
                            c_obj = pg_session.query(Concept).filter_by(chapter_id=ch_obj.id, name=con.get("concept_name")).first()
                            if not c_obj:
                                c_obj = Concept(
                                    chapter_id=ch_obj.id,
                                    name=con.get("concept_name"),
                                    description=con.get("explanation", {}).get("standard", ""),
                                    difficulty_level=float(con.get("difficulty", 1.0))
                                )
                                pg_session.add(c_obj)
                                pg_session.commit()
                                pg_session.refresh(c_obj)

                            # Add learning objectives
                            for obj_text in con.get("learning_objectives", []):
                                lo = pg_session.query(LearningObjective).filter_by(concept_id=c_obj.id, description=obj_text).first()
                                if not lo:
                                    lo = LearningObjective(concept_id=c_obj.id, description=obj_text)
                                    pg_session.add(lo)
                                    pg_session.commit()
                                    pg_session.refresh(lo)

                                # Add questions
                                for q in con.get("questions", []):
                                    q_obj = pg_session.query(Question).filter_by(objective_id=lo.id, base_text=q.get("prompt")).first()
                                    if not q_obj:
                                        q_obj = Question(
                                            objective_id=lo.id,
                                            base_text=q.get("prompt"),
                                            question_type=q.get("question_type", "multiple_choice"),
                                            difficulty=float(q.get("difficulty", 1.0))
                                        )
                                        pg_session.add(q_obj)
                                        pg_session.commit()
                                        pg_session.refresh(q_obj)

                                        # Add variant
                                        qv = QuestionVariant(
                                            question_id=q_obj.id,
                                            content={
                                                "options": q.get("options", []),
                                                "answer": q.get("correct_answer"),
                                                "explanation": q.get("explanation"),
                                                "hints": q.get("hints", [])
                                            },
                                            sensory_adaptation="standard"
                                        )
                                        pg_session.add(qv)
                                        pg_session.commit()

            pg_session.close()
            print("[OK] Successfully Seeded PostgreSQL Relational Tables (Subjects, Chapters, Concepts, Objectives, Questions).")
        except Exception as e:
            print(f"[NOTICE] PostgreSQL Relational Seeding Notice: {e}")

    print("==========================================================================")

if __name__ == "__main__":
    asyncio.run(seed_knowledge_graph())
