import os
import sys
import asyncio
from datetime import datetime

# Add backend directory to sys.path
sys.path.insert(0, os.path.join(os.getcwd(), "backend"))

from sqlalchemy import text
from app.database import engine, get_database
from app.services.seed_service import seed_database_content, SEED_TASKS, SEED_BADGES, DEMO_PROFILES
from app.routers.students import compute_baseline_support_dimensions

async def sanitize_and_configure_database():
    print("==========================================================")
    print("CONFIGURING CLEAN CANONICAL DATABASE")
    print("==========================================================")

    # 1. PostgreSQL Cleanup
    if engine is not None:
        with engine.connect() as conn:
            print("\n[1] Sanitizing PostgreSQL Relational Tables...")

            # Clean duplicate / test learners, keeping only the primary one for jeeva
            conn.execute(text("""
                DELETE FROM learners 
                WHERE id NOT IN (
                    SELECT MIN(id) FROM learners WHERE name = 'Aarav Sharma'
                ) AND name = 'Aarav Sharma'
            """))

            conn.execute(text("""
                DELETE FROM learners WHERE name LIKE 'Test%'
            """))

            # Delete all ephemeral audit, verification, and temporary test users
            conn.execute(text("""
                DELETE FROM users 
                WHERE username LIKE 'audit_user_%'
                   OR username LIKE 'verify_ds_%'
                   OR username LIKE 'temp_tester%'
                   OR username LIKE 'caregiver_qa_%'
                   OR username LIKE 'newuser_%'
            """))
            conn.commit()

            # Verify remaining users and learners
            users = conn.execute(text("SELECT id, username, email, role FROM users")).fetchall()
            print(f"  [RETAINED] {len(users)} Canonical Users:")
            for u in users:
                print(f"    - ID {u[0]}: {u[1]} ({u[2]}) [{u[3]}]")

            learners = conn.execute(text("SELECT id, caregiver_id, name FROM learners")).fetchall()
            print(f"  [RETAINED] {len(learners)} Canonical Students:")
            for l in learners:
                print(f"    - ID {l[0]}: {l[2]} (Caregiver ID: {l[1]})")

    # 2. MongoDB Cleanup & Canonical Seeding
    print("\n[2] Sanitizing and Seeding MongoDB Collections...")
    db = get_database()

    # Re-seed canonical tasks and badges
    await seed_database_content()

    # Ensure canonical baseline support profile for Aarav Sharma exists
    canonical_responses = {
        "q1": "Often",
        "q2": "Often",
        "q3": "Often",
        "q4": "Very Often",
        "q5": "Very challenging",
        "q6": "Extremely helpful",
        "q7": "Needs extended time to think before answering",
        "q8": "High — visual motion or moving elements break focus",
        "q9": "Single-concept focus (one idea and one action per screen)",
        "q10": "Micro-challenges (1 to 2 minutes each)",
        "q11": "Needs frequent reinforcement through varied examples",
        "q12": "Completely untimed, relaxed exploration",
        "q13": "Gentle, non-punitive nudges with instant first-step hints",
        "q14": "Interactive visual diagrams with optional audio read-aloud",
        "q15": "Break multi-step activities into step-by-step sequential cards",
        "q16": "High visual support with generous whitespace and clear contrast",
        "q17": "On-demand audio reader button for any text passage",
        "q18": "Immediate celebratory feedback without countdown pressure",
        "q19": "Revisit concepts using high-interest analogies (Space, Science)",
        "q20": "Clear completion checkpoints with optional 1-minute sensory rest pauses"
    }

    # Clean test records from MongoDB
    await db["users"].delete_many({
        "$or": [
            {"username": {"$regex": "^audit_user_"}},
            {"username": {"$regex": "^verify_ds_"}},
            {"email": {"$regex": "@example\\.com$"}},
            {"email": {"$regex": "@test\\.com$"}}
        ]
    })

    # Clean duplicate learners in Mongo
    aarav_docs = await db["learners"].find({"name": "Aarav Sharma"}).to_list(length=10)
    if len(aarav_docs) > 1:
        keep_id = aarav_docs[0]["_id"]
        await db["learners"].delete_many({
            "name": "Aarav Sharma",
            "_id": {"$ne": keep_id}
        })
        print("  Cleaned duplicate Aarav Sharma documents in MongoDB.")

    # Canonical baseline profile for student
    aarav_student = await db["learners"].find_one({"name": "Aarav Sharma"})
    student_id = str(aarav_student.get("_id", aarav_student.get("id", "aarav_sharma"))) if aarav_student else "aarav_sharma"
    caretaker_id = str(aarav_student.get("caretaker_id", aarav_student.get("caregiver_id", "jeeva"))) if aarav_student else "jeeva"

    aarav_profile = compute_baseline_support_dimensions(
        student_id=student_id,
        student_name="Aarav Sharma",
        caretaker_id=caretaker_id,
        responses=canonical_responses
    )
    await db["baseline_support_profiles"].update_one(
        {"student_id": student_id},
        {"$set": aarav_profile.model_dump()},
        upsert=True
    )

    # Demo baseline profiles for Leo, Maya, Kai
    for demo in DEMO_PROFILES:
        demo_b = compute_baseline_support_dimensions(
            student_id=demo["learner_id"],
            student_name=demo["learner_name"],
            caretaker_id=demo["caregiver_id"],
            responses={"q1": "Often", "q2": "Often", "q3": "Often", "q4": "Very Often", "q5": "Very challenging"}
        )
        await db["baseline_support_profiles"].update_one(
            {"student_id": demo["learner_id"]},
            {"$set": demo_b.model_dump()},
            upsert=True
        )

    tasks_count = await db["tasks"].count_documents({})
    badges_count = await db["rewards"].count_documents({})
    profiles_count = await db["baseline_support_profiles"].count_documents({})
    prefs_count = await db["learner_preferences"].count_documents({})

    print(f"  [MONGODB] Tasks Collection: {tasks_count} tasks")
    print(f"  [MONGODB] Badges/Rewards: {badges_count} badges")
    print(f"  [MONGODB] Baseline Support Profiles: {profiles_count} profiles")
    print(f"  [MONGODB] Learner Preferences: {prefs_count} profiles")

    print("\n==========================================================")
    print("CANONICAL DATABASE SANITIZATION COMPLETE!")
    print("==========================================================")

if __name__ == "__main__":
    asyncio.run(sanitize_and_configure_database())
