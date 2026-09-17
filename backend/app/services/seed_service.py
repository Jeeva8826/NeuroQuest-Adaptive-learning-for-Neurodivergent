import logging
from app.database import get_database

logger = logging.getLogger("neuroquest.seed_service")

SEED_TASKS = [
    # MATHEMATICS
    {
        "title": "Space Star Counting",
        "subject": "Mathematics",
        "difficulty": 1,
        "estimated_duration": 3,
        "question": "An astronaut explorer saw 4 blue stars and 3 yellow stars in deep space. How many stars did they count in total?",
        "content_type": "multiple_choice",
        "options": ["5 stars", "6 stars", "7 stars", "8 stars"],
        "correct_answer": "7 stars",
        "explanation": "4 blue stars + 3 yellow stars = 7 total stars!",
        "hints": [
            "Start with the 4 blue stars.",
            "Count 3 more yellow stars: 5, 6, 7!",
            "4 + 3 = 7."
        ],
        "steps": [
            {"step_number": 1, "title": "Group blue stars", "description": "Count 4 blue stars", "hint": "Use your fingers or visual counter."},
            {"step_number": 2, "title": "Add yellow stars", "description": "Add 3 yellow stars to 4", "hint": "4 + 3 = 7."}
        ],
        "supported_learning_modes": ["Seeing", "Doing", "Listening"],
        "theme_tags": ["space", "animals", "general"],
        "icon_name": "Calculator"
    },
    {
        "title": "Cosmic Pattern Helper",
        "subject": "Mathematics",
        "difficulty": 2,
        "estimated_duration": 4,
        "question": "Look at the pattern: 2, 4, 6, 8, __. What is the next number?",
        "content_type": "multiple_choice",
        "options": ["9", "10", "11", "12"],
        "correct_answer": "10",
        "explanation": "Each number increases by 2! 8 + 2 = 10.",
        "hints": [
            "Notice how much each number jumps.",
            "2 + 2 = 4, 4 + 2 = 6, 6 + 2 = 8.",
            "Add 2 to 8."
        ],
        "steps": [],
        "supported_learning_modes": ["Seeing", "Reading"],
        "theme_tags": ["coding", "space", "general"],
        "icon_name": "Sparkles"
    },
    
    # SCIENCE
    {
        "title": "Animal Habitat Explorer",
        "subject": "Science",
        "difficulty": 1,
        "estimated_duration": 4,
        "question": "Which habitat is home to creatures like dolphins, sea turtles, and clownfish?",
        "content_type": "multiple_choice",
        "options": ["Desert", "Ocean", "Forest", "Mountain"],
        "correct_answer": "Ocean",
        "explanation": "Dolphins, sea turtles, and clownfish live in salt water ocean environments!",
        "hints": [
            "Think about where saltwater creatures swim.",
            "It is a vast body of blue water covering most of Earth."
        ],
        "steps": [],
        "supported_learning_modes": ["Seeing", "Listening", "Reading"],
        "theme_tags": ["animals", "nature"],
        "icon_name": "Globe"
    },
    {
        "title": "Solar System Giant",
        "subject": "Science",
        "difficulty": 2,
        "estimated_duration": 5,
        "question": "Which planet in our solar system is famous for its massive ring system?",
        "content_type": "multiple_choice",
        "options": ["Mars", "Saturn", "Mercury", "Venus"],
        "correct_answer": "Saturn",
        "explanation": "Saturn is known for its beautiful rings made of ice, dust, and rock particles!",
        "hints": [
            "It is the 6th planet from the Sun.",
            "Its bright rings can be seen with a telescope."
        ],
        "steps": [],
        "supported_learning_modes": ["Seeing", "Reading"],
        "theme_tags": ["space", "general"],
        "icon_name": "Sun"
    },
    
    # ENGLISH
    {
        "title": "Kind Words & Descriptions",
        "subject": "English",
        "difficulty": 1,
        "estimated_duration": 3,
        "question": "Choose the word that describes a dog that loves running, playing catch, and wagging its tail happily.",
        "content_type": "multiple_choice",
        "options": ["Playful", "Sleepy", "Quiet", "Heavy"],
        "correct_answer": "Playful",
        "explanation": "'Playful' describes someone full of energy and fun!",
        "hints": [
            "The dog loves running and playing games.",
            "It starts with 'Play'."
        ],
        "steps": [],
        "supported_learning_modes": ["Listening", "Reading"],
        "theme_tags": ["animals", "general", "stories"],
        "icon_name": "BookOpen"
    },
    {
        "title": "Rhyme Time Adventure",
        "subject": "English",
        "difficulty": 1,
        "estimated_duration": 3,
        "question": "Which word rhymes with 'BRIGHT' and 'NIGHT'?",
        "content_type": "multiple_choice",
        "options": ["LIGHT", "MOON", "DARK", "STAR"],
        "correct_answer": "LIGHT",
        "explanation": "BRIGHT, NIGHT, and LIGHT all end in the '-ight' sound!",
        "hints": [
            "Listen closely to the ending sound of 'BRIGHT'.",
            "L - IGHT rhymes with N - IGHT."
        ],
        "steps": [],
        "supported_learning_modes": ["Listening", "Doing"],
        "theme_tags": ["music", "fantasy", "space"],
        "icon_name": "Music"
    },

    # GENERAL KNOWLEDGE
    {
        "title": "Colors of the Rainbow",
        "subject": "General Knowledge",
        "difficulty": 1,
        "estimated_duration": 3,
        "question": "When sunlight passes through raindrops in the sky, what beautiful natural arch appears?",
        "content_type": "multiple_choice",
        "options": ["Rainbow", "Lightning bolt", "Comet tail", "Tornado"],
        "correct_answer": "Rainbow",
        "explanation": "A rainbow forms when sunlight bends and reflects through water droplets!",
        "hints": [
            "It features red, orange, yellow, green, blue, indigo, and violet.",
            "It appears in the sky after a gentle rain shower."
        ],
        "steps": [],
        "supported_learning_modes": ["Seeing", "Reading"],
        "theme_tags": ["art", "nature"],
        "icon_name": "Palette"
    },

    # CODING / LOGIC
    {
        "title": "Robot Navigator Command",
        "subject": "Coding/Logic",
        "difficulty": 1,
        "estimated_duration": 5,
        "question": "Help Robot Sparky reach the battery charging pad! Sparky takes 2 steps forward, turns right, and takes 1 step forward. What sequence of commands is that?",
        "content_type": "multiple_choice",
        "options": [
            "FORWARD, FORWARD, TURN RIGHT, FORWARD",
            "TURN RIGHT, FORWARD, FORWARD",
            "FORWARD, TURN LEFT, FORWARD",
            "BACKWARD, FORWARD, TURN RIGHT"
        ],
        "correct_answer": "FORWARD, FORWARD, TURN RIGHT, FORWARD",
        "explanation": "Step 1: Forward, Step 2: Forward, Step 3: Turn Right, Step 4: Forward!",
        "hints": [
            "Break the journey down step by step.",
            "First 2 steps move FORWARD, then TURN RIGHT, then 1 step FORWARD."
        ],
        "steps": [
            {"step_number": 1, "title": "First 2 Steps", "description": "Move FORWARD twice.", "hint": "FORWARD, FORWARD"},
            {"step_number": 2, "title": "Change Direction", "description": "TURN RIGHT to face pad.", "hint": "TURN RIGHT"},
            {"step_number": 3, "title": "Final Step", "description": "Move FORWARD onto pad.", "hint": "FORWARD"}
        ],
        "supported_learning_modes": ["Doing", "Seeing"],
        "theme_tags": ["coding", "space", "games"],
        "icon_name": "Cpu"
    }
]

SEED_BADGES = [
    {
        "id": "star_explorer",
        "title": "Star Explorer",
        "description": "Completed your first learning activity on NeuroQuest!",
        "icon": "Star",
        "category": "achievement",
        "is_unlocked": True
    },
    {
        "id": "theme_master",
        "title": "World Creator",
        "description": "Personalized your learning theme and preferences!",
        "icon": "Palette",
        "category": "personalization",
        "is_unlocked": True
    },
    {
        "id": "math_wizard",
        "title": "Number Navigator",
        "description": "Solved a Mathematics quest with cosmic clarity!",
        "icon": "Calculator",
        "category": "subject",
        "is_unlocked": False
    },
    {
        "id": "logic_pioneer",
        "title": "Logic Pioneer",
        "description": "Guided Robot Sparky through a code maze!",
        "icon": "Cpu",
        "category": "subject",
        "is_unlocked": False
    }
]

DEMO_PROFILES = [
    {
        "learner_id": "demo_learner_a",
        "caregiver_id": "demo_caregiver",
        "learner_name": "Leo (Space Explorer)",
        "learner_age": 9,
        "interests": ["Space", "Rockets", "Astronomy"],
        "hobbies": ["Stargazing", "Building space Lego"],
        "preferred_learning_modes": ["Seeing", "Doing"],
        "visual_preferences": {
            "favorite_colors": ["purple", "indigo"],
            "avoided_colors": ["red"],
            "palette_type": "soft",
            "visual_style": "pictures",
            "primary_color": "#8b5cf6",
            "secondary_color": "#3b82f6",
            "background_theme": "space",
            "font_family": "rounded",
            "font_scale": "medium"
        },
        "sensory_preferences": {
            "sound_enabled": True,
            "sound_preference": "calm_chimes",
            "animation_intensity": "low",
            "visual_density": "spacious",
            "calm_mode": True
        },
        "motivation": {
            "preferred_rewards": ["Unlocking something", "Exploration nodes"],
            "reward_style": "exploration"
        },
        "gamification": {
            "motivation_types": ["exploration"],
            "game_theme": "space",
            "reward_preference": "unlockables",
            "interaction_preference": "step_by_step",
            "celebration_preference": "gentle_sparkles",
            "progress_style": "exploration_map"
        },
        "interaction_preferences": {
            "task_size": "small",
            "feedback_style": "immediate",
            "guidance_level": "high",
            "break_frequency_mins": 10
        }
    },
    {
        "learner_id": "demo_learner_b",
        "caregiver_id": "demo_caregiver",
        "learner_name": "Maya (Wildlife Ranger)",
        "learner_age": 8,
        "interests": ["Animals", "Nature", "Sanctuary"],
        "hobbies": ["Drawing animals", "Watching nature films"],
        "preferred_learning_modes": ["Listening", "Seeing"],
        "visual_preferences": {
            "favorite_colors": ["teal", "emerald"],
            "avoided_colors": [],
            "palette_type": "soft",
            "visual_style": "pictures",
            "primary_color": "#10b981",
            "secondary_color": "#14b8a6",
            "background_theme": "animals",
            "font_family": "sans",
            "font_scale": "medium"
        },
        "sensory_preferences": {
            "sound_enabled": True,
            "sound_preference": "quiet",
            "animation_intensity": "normal",
            "visual_density": "spacious",
            "calm_mode": True
        },
        "motivation": {
            "preferred_rewards": ["Collecting objects", "Animal cards"],
            "reward_style": "collectables"
        },
        "gamification": {
            "motivation_types": ["collection"],
            "game_theme": "animals",
            "reward_preference": "collectibles",
            "interaction_preference": "visual_audio",
            "celebration_preference": "sound_chime",
            "progress_style": "mastery_tree"
        },
        "interaction_preferences": {
            "task_size": "small",
            "feedback_style": "immediate",
            "guidance_level": "moderate",
            "break_frequency_mins": 12
        }
    },
    {
        "learner_id": "demo_learner_c",
        "caregiver_id": "demo_caregiver",
        "learner_name": "Kai (Cyber Engineer)",
        "learner_age": 11,
        "interests": ["Coding/Technology", "Robots", "Gadgets"],
        "hobbies": ["Scratch coding", "Robot building"],
        "preferred_learning_modes": ["Doing", "Interactive"],
        "visual_preferences": {
            "favorite_colors": ["blue", "sky"],
            "avoided_colors": [],
            "palette_type": "high_contrast",
            "visual_style": "diagrams",
            "primary_color": "#0284c7",
            "secondary_color": "#6366f1",
            "background_theme": "coding",
            "font_family": "sans",
            "font_scale": "medium"
        },
        "sensory_preferences": {
            "sound_enabled": False,
            "sound_preference": "quiet",
            "animation_intensity": "low",
            "visual_density": "balanced",
            "calm_mode": False
        },
        "motivation": {
            "preferred_rewards": ["Robot parts", "Building components"],
            "reward_style": "building"
        },
        "gamification": {
            "motivation_types": ["building"],
            "game_theme": "coding",
            "reward_preference": "components",
            "interaction_preference": "interactive",
            "celebration_preference": "visual_banner",
            "progress_style": "mastery_tree"
        },
        "interaction_preferences": {
            "task_size": "medium",
            "feedback_style": "summary",
            "guidance_level": "moderate",
            "break_frequency_mins": 15
        }
    }
]

async def seed_database_content():
    db = get_database()
    
    # Check if tasks collection has items
    existing_tasks_count = await db["tasks"].count_documents({})
    if existing_tasks_count == 0:
        logger.info("Seeding initial learning tasks into MongoDB...")
        await db["tasks"].insert_many(SEED_TASKS)
        logger.info(f"Successfully seeded {len(SEED_TASKS)} tasks.")
    else:
        logger.info(f"Tasks collection already populated ({existing_tasks_count} tasks).")

    # Check if rewards/badges collection exists
    existing_badges_count = await db["rewards"].count_documents({})
    if existing_badges_count == 0:
        logger.info("Seeding initial rewards badges into MongoDB...")
        await db["rewards"].insert_many(SEED_BADGES)
        logger.info(f"Successfully seeded {len(SEED_BADGES)} badges.")
    else:
        logger.info(f"Badges collection already populated ({existing_badges_count} badges).")

    # Seed Demo Learner Profiles
    for profile in DEMO_PROFILES:
        await db["learner_preferences"].update_one(
            {"learner_id": profile["learner_id"]},
            {"$set": profile},
            upsert=True
        )
    logger.info("Successfully seeded 3 Hackathon Demo Learner Profiles (Learner A, B, C).")

