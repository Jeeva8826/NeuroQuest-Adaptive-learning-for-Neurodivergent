-- ==========================================================
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
    grade INTEGER,
    standard VARCHAR(50),
    chapter VARCHAR(255),
    difficulty INTEGER,
    estimated_duration INTEGER,
    question TEXT,
    content_type VARCHAR(100),
    options JSONB,
    correct_answer TEXT,
    explanation TEXT,
    hints JSONB,
    scaffold_steps JSONB,
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
