import os
import sys
import csv
import json

# Add backend directory to sys.path
sys.path.insert(0, os.path.join(os.getcwd(), "backend"))

import pandas as pd
from sqlalchemy import create_engine, text, inspect
from app.config import settings
from app.database import engine, get_database
from app.services.seed_service import seed_database_content, SEED_TASKS, SEED_BADGES, DEMO_PROFILES
from app.routers.students import compute_baseline_support_dimensions
import asyncio

OUTPUT_DIR = os.path.join(os.getcwd(), "exports", "neon_csv")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def export_postgres_tables():
    print("=== Exporting PostgreSQL Relational Tables to CSV ===")
    if engine is None:
        print("Engine not found.")
        return []
    
    exported_files = []
    insp = inspect(engine)
    table_names = insp.get_table_names()

    with engine.connect() as conn:
        for tbl in table_names:
            query = f"SELECT * FROM {tbl}"
            df = pd.read_sql(query, conn)
            
            # Serialize JSON/dict columns to strings so Postgres/Neon CSV importer handles them cleanly
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else x)
            
            csv_path = os.path.join(OUTPUT_DIR, f"{tbl}.csv")
            df.to_csv(csv_path, index=False, quoting=csv.QUOTE_MINIMAL)
            row_count = len(df)
            exported_files.append((tbl, csv_path, row_count))
            print(f"  [SAVED] {tbl}.csv ({row_count} rows) -> {csv_path}")

    return exported_files

async def export_mongo_collections():
    print("\n=== Exporting MongoDB Collections to CSV ===")
    exported_files = []
    
    # Seed MongoDB with tasks, badges, demo profiles and NCERT knowledge graph
    try:
        await seed_database_content()
    except Exception as e:
        print(f"Seed note: {e}")
    
    db = get_database()
    
    # 1. Tasks
    tasks_cursor = db["tasks"].find({})
    tasks_list = await tasks_cursor.to_list(length=200)
    if not tasks_list:
        tasks_list = SEED_TASKS
    
    clean_tasks = []
    for t in tasks_list:
        clean_tasks.append({
            "id": str(t.get("_id", t.get("id", ""))),
            "title": t.get("title", ""),
            "subject": t.get("subject", ""),
            "difficulty": t.get("difficulty", 1),
            "estimated_duration": t.get("estimated_duration", 3),
            "question": t.get("question", ""),
            "content_type": t.get("content_type", "multiple_choice"),
            "options": json.dumps(t.get("options", [])),
            "correct_answer": t.get("correct_answer", ""),
            "explanation": t.get("explanation", ""),
            "hints": json.dumps(t.get("hints", [])),
            "supported_learning_modes": json.dumps(t.get("supported_learning_modes", [])),
            "theme_tags": json.dumps(t.get("theme_tags", [])),
            "icon_name": t.get("icon_name", "Sparkles")
        })
    df_tasks = pd.DataFrame(clean_tasks)
    tasks_csv = os.path.join(OUTPUT_DIR, "curriculum_tasks.csv")
    df_tasks.to_csv(tasks_csv, index=False)
    exported_files.append(("curriculum_tasks", tasks_csv, len(df_tasks)))
    print(f"  [SAVED] curriculum_tasks.csv ({len(df_tasks)} rows) -> {tasks_csv}")

    # 2. Baseline Support Profiles
    profiles_cursor = db["baseline_support_profiles"].find({})
    profiles_list = await profiles_cursor.to_list(length=200)
    if not profiles_list:
        # Create baseline support profiles for demo learners
        profiles_list = []
        for demo in DEMO_PROFILES:
            b_prof = compute_baseline_support_dimensions(
                student_id=demo["learner_id"],
                student_name=demo["learner_name"],
                caretaker_id=demo["caregiver_id"],
                responses={"q1": "Often", "q2": "Often", "q3": "Often", "q4": "Very Often", "q5": "Very challenging"}
            )
            profiles_list.append(b_prof.model_dump())

    clean_profiles = []
    for p in profiles_list:
        clean_profiles.append({
            "student_id": p.get("student_id"),
            "student_name": p.get("student_name"),
            "caretaker_id": p.get("caretaker_id"),
            "version": p.get("version", "baseline-v1"),
            "attention_support": p.get("attention_support"),
            "instruction_style": p.get("instruction_style"),
            "information_density_support": p.get("information_density_support"),
            "content_representation": p.get("content_representation"),
            "task_granularity": p.get("task_granularity"),
            "pace_support": p.get("pace_support"),
            "scaffolding_support": p.get("scaffolding_support"),
            "feedback_support": p.get("feedback_support"),
            "repetition_support": p.get("repetition_support"),
            "transition_support": p.get("transition_support"),
            "recommended_accommodations": json.dumps(p.get("recommended_accommodations", [])),
            "initial_ui_configuration": json.dumps(p.get("initial_ui_configuration", {})),
            "disclaimer": p.get("disclaimer", "")
        })
    df_prof = pd.DataFrame(clean_profiles)
    prof_csv = os.path.join(OUTPUT_DIR, "baseline_support_profiles.csv")
    df_prof.to_csv(prof_csv, index=False)
    exported_files.append(("baseline_support_profiles", prof_csv, len(df_prof)))
    print(f"  [SAVED] baseline_support_profiles.csv ({len(df_prof)} rows) -> {prof_csv}")

    # 3. Badges / Rewards
    badges_cursor = db["badges"].find({})
    badges_list = await badges_cursor.to_list(length=200)
    if not badges_list:
        rewards_cursor = db["rewards"].find({})
        badges_list = await rewards_cursor.to_list(length=200)
    if not badges_list:
        badges_list = SEED_BADGES
    clean_badges = []
    for b in badges_list:
        clean_badges.append({
            "badge_id": b.get("id", b.get("badge_id", "")),
            "name": b.get("title", b.get("name", "")),
            "description": b.get("description", ""),
            "icon": b.get("icon", "Award"),
            "category": b.get("category", "Milestone")
        })
    df_badges = pd.DataFrame(clean_badges)
    badges_csv = os.path.join(OUTPUT_DIR, "badges.csv")
    df_badges.to_csv(badges_csv, index=False)
    exported_files.append(("badges", badges_csv, len(df_badges)))
    print(f"  [SAVED] badges.csv ({len(df_badges)} rows) -> {badges_csv}")

    # 4. Learner Preferences
    pref_cursor = db["learner_preferences"].find({})
    pref_list = await pref_cursor.to_list(length=200)
    if pref_list:
        clean_prefs = []
        for p in pref_list:
            clean_prefs.append({
                "learner_id": p.get("learner_id", ""),
                "caregiver_id": p.get("caregiver_id", ""),
                "learner_name": p.get("learner_name", ""),
                "learner_age": p.get("learner_age", 8),
                "interests": json.dumps(p.get("interests", [])),
                "hobbies": json.dumps(p.get("hobbies", [])),
                "preferred_learning_modes": json.dumps(p.get("preferred_learning_modes", [])),
                "visual_preferences": json.dumps(p.get("visual_preferences", {})),
                "sensory_preferences": json.dumps(p.get("sensory_preferences", {})),
                "motivation": json.dumps(p.get("motivation", {})),
                "gamification": json.dumps(p.get("gamification", {})),
                "interaction_preferences": json.dumps(p.get("interaction_preferences", {}))
            })
        df_pref = pd.DataFrame(clean_prefs)
        pref_csv = os.path.join(OUTPUT_DIR, "learner_preferences.csv")
        df_pref.to_csv(pref_csv, index=False)
        exported_files.append(("learner_preferences", pref_csv, len(df_pref)))
        print(f"  [SAVED] learner_preferences.csv ({len(df_pref)} rows) -> {pref_csv}")

    return exported_files

def generate_neon_ddl():
    """Generates a clean neon_schema.sql file that can be pasted into Neon's SQL Editor"""
    sql_path = os.path.join(OUTPUT_DIR, "neon_schema.sql")
    sql_content = """-- ==========================================================
-- NEUROQUEST RELATIONAL SCHEMA FOR NEON CLOUD POSTGRESQL
-- Paste this script directly into the Neon Console SQL Editor!
-- ==========================================================

-- 1. Create Enums
DO $$ BEGIN
    CREATE TYPE user_role AS ENUM ('CAREGIVER', 'EDUCATOR', 'ADMIN');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- 2. Users Table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE,
    hashed_password TEXT,
    role VARCHAR(50) DEFAULT 'CAREGIVER',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Learners Table
CREATE TABLE IF NOT EXISTS learners (
    id SERIAL PRIMARY KEY,
    caregiver_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255),
    date_of_birth TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Caregiver Profiles
CREATE TABLE IF NOT EXISTS caregiver_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    questionnaire_completed BOOLEAN DEFAULT FALSE,
    questionnaire_responses JSONB
);

-- 5. Support Preferences
CREATE TABLE IF NOT EXISTS support_preferences (
    id SERIAL PRIMARY KEY,
    learner_id INTEGER REFERENCES learners(id) ON DELETE CASCADE,
    visual_support_level INTEGER,
    audio_support_level INTEGER,
    repetition_needs INTEGER,
    feedback_style VARCHAR(255),
    sensory_preferences JSONB
);

-- 6. Subjects Table
CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    description TEXT
);

-- 7. Chapters Table
CREATE TABLE IF NOT EXISTS chapters (
    id SERIAL PRIMARY KEY,
    subject_id INTEGER REFERENCES subjects(id) ON DELETE CASCADE,
    title VARCHAR(255),
    order_index INTEGER
);

-- 8. Concepts Table
CREATE TABLE IF NOT EXISTS concepts (
    id SERIAL PRIMARY KEY,
    chapter_id INTEGER REFERENCES chapters(id) ON DELETE CASCADE,
    name VARCHAR(255),
    description TEXT,
    difficulty_level FLOAT
);

-- 9. Learning Objectives
CREATE TABLE IF NOT EXISTS learning_objectives (
    id SERIAL PRIMARY KEY,
    concept_id INTEGER REFERENCES concepts(id) ON DELETE CASCADE,
    description TEXT
);

-- 10. Questions Table
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    objective_id INTEGER REFERENCES learning_objectives(id) ON DELETE CASCADE,
    base_text TEXT,
    question_type VARCHAR(100),
    difficulty FLOAT
);

-- 11. Question Variants Table
CREATE TABLE IF NOT EXISTS question_variants (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    content JSONB,
    sensory_adaptation VARCHAR(255)
);

-- 12. Curriculum Tasks (Interactive NCERT tasks)
CREATE TABLE IF NOT EXISTS curriculum_tasks (
    id VARCHAR(100) PRIMARY KEY,
    title VARCHAR(255),
    subject VARCHAR(100),
    difficulty INTEGER,
    estimated_duration INTEGER,
    question TEXT,
    content_type VARCHAR(100),
    options JSONB,
    correct_answer TEXT,
    explanation TEXT,
    hints JSONB,
    supported_learning_modes JSONB,
    theme_tags JSONB,
    icon_name VARCHAR(100)
);

-- 13. Baseline Support Profiles (Student Baseline v1)
CREATE TABLE IF NOT EXISTS baseline_support_profiles (
    id SERIAL PRIMARY KEY,
    student_id VARCHAR(100),
    student_name VARCHAR(255),
    caretaker_id VARCHAR(100),
    version VARCHAR(50) DEFAULT 'baseline-v1',
    attention_support TEXT,
    instruction_style TEXT,
    information_density_support TEXT,
    content_representation TEXT,
    task_granularity TEXT,
    pace_support TEXT,
    scaffolding_support TEXT,
    feedback_support TEXT,
    repetition_support TEXT,
    transition_support TEXT,
    recommended_accommodations JSONB,
    initial_ui_configuration JSONB,
    disclaimer TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 14. Badges
CREATE TABLE IF NOT EXISTS badges (
    id SERIAL PRIMARY KEY,
    badge_id VARCHAR(100),
    name VARCHAR(255),
    description TEXT,
    icon VARCHAR(100),
    category VARCHAR(100)
);

-- 15. Learner Preferences
CREATE TABLE IF NOT EXISTS learner_preferences (
    id SERIAL PRIMARY KEY,
    learner_id VARCHAR(100),
    caregiver_id VARCHAR(100),
    learner_name VARCHAR(255),
    learner_age INTEGER,
    interests JSONB,
    hobbies JSONB,
    preferred_learning_modes JSONB,
    visual_preferences JSONB,
    sensory_preferences JSONB,
    motivation JSONB,
    gamification JSONB,
    interaction_preferences JSONB
);

-- 16. Concept Prerequisites
CREATE TABLE IF NOT EXISTS concept_prerequisites (
    id SERIAL PRIMARY KEY,
    concept_id INTEGER REFERENCES concepts(id) ON DELETE CASCADE,
    prerequisite_id INTEGER REFERENCES concepts(id) ON DELETE CASCADE
);

-- 17. Learner Mastery (BKT)
CREATE TABLE IF NOT EXISTS learner_mastery (
    id SERIAL PRIMARY KEY,
    learner_id INTEGER REFERENCES learners(id) ON DELETE CASCADE,
    concept_id INTEGER REFERENCES concepts(id) ON DELETE CASCADE,
    p_known FLOAT DEFAULT 0.1,
    p_guess FLOAT DEFAULT 0.2,
    p_slip FLOAT DEFAULT 0.1,
    p_transit FLOAT DEFAULT 0.1,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 18. Learning Events
CREATE TABLE IF NOT EXISTS learning_events (
    id SERIAL PRIMARY KEY,
    learner_id INTEGER REFERENCES learners(id) ON DELETE CASCADE,
    event_type VARCHAR(100),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    payload JSONB
);

-- 19. Question Attempts
CREATE TABLE IF NOT EXISTS question_attempts (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES learning_events(id) ON DELETE CASCADE,
    variant_id INTEGER REFERENCES question_variants(id) ON DELETE CASCADE,
    is_correct BOOLEAN,
    response_time_ms INTEGER
);

-- 20. Adaptations
CREATE TABLE IF NOT EXISTS adaptations (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES learning_events(id) ON DELETE CASCADE,
    adaptation_type VARCHAR(100),
    applied_changes JSONB
);

-- 21. Adaptation Feedback
CREATE TABLE IF NOT EXISTS adaptation_feedback (
    id SERIAL PRIMARY KEY,
    adaptation_id INTEGER REFERENCES adaptations(id) ON DELETE CASCADE,
    success_rating FLOAT
);

-- 22. Scaffolds
CREATE TABLE IF NOT EXISTS scaffolds (
    id SERIAL PRIMARY KEY,
    variant_id INTEGER REFERENCES question_variants(id) ON DELETE CASCADE,
    scaffold_level INTEGER,
    content JSONB
);

-- 23. Game Sessions
CREATE TABLE IF NOT EXISTS game_sessions (
    id SERIAL PRIMARY KEY,
    learner_id INTEGER REFERENCES learners(id) ON DELETE CASCADE,
    started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP WITH TIME ZONE,
    device_info JSONB
);

-- 24. Game Events
CREATE TABLE IF NOT EXISTS game_events (
    id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES game_sessions(id) ON DELETE CASCADE,
    action_type VARCHAR(100),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    event_data JSONB
);

-- 25. Content Sources & Licenses
CREATE TABLE IF NOT EXISTS content_sources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    url TEXT
);

CREATE TABLE IF NOT EXISTS content_licenses (
    id SERIAL PRIMARY KEY,
    source_id INTEGER REFERENCES content_sources(id) ON DELETE CASCADE,
    license_type VARCHAR(100)
);
"""
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(sql_content)
    print(f"\n  [SAVED] neon_schema.sql DDL script -> {sql_path}")

if __name__ == "__main__":
    pg_files = export_postgres_tables()
    m_files = asyncio.run(export_mongo_collections())
    generate_neon_ddl()
    print("\n==========================================================")
    print(f"DATABASE EXPORT COMPLETE! All files are in: {OUTPUT_DIR}")
    print("==========================================================")
