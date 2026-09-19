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
    },

    # NCERT CLASS 7 SCIENCE (CHAPTER 1): NUTRITION IN PLANTS
    {
        "title": "Photosynthesis Oxygen Factory",
        "subject": "Science",
        "difficulty": 1,
        "estimated_duration": 4,
        "question": "In NCERT Chapter 1, green plants use sunlight and carbon dioxide to make food. What vital gas do they release into the air for astronauts and animals to breathe?",
        "content_type": "multiple_choice",
        "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Helium"],
        "correct_answer": "Oxygen",
        "explanation": "During photosynthesis, plants take in carbon dioxide and water using solar energy captured by chlorophyll, releasing vital oxygen into the atmosphere!",
        "hints": [
            "Think about the gas animals breathe in every day.",
            "Leaves absorb carbon dioxide and give off this gas in daylight.",
            "It begins with the letter 'O'."
        ],
        "steps": [
            {"step_number": 1, "title": "Plant Inhalation", "description": "Leaves absorb Carbon Dioxide and Water through stomata.", "hint": "CO2 goes in."},
            {"step_number": 2, "title": "Solar Reaction", "description": "Chlorophyll traps sunlight to power the chemical reaction.", "hint": "Light energy converts molecules."},
            {"step_number": 3, "title": "Life Release", "description": "Oxygen is produced as a byproduct and released.", "hint": "Oxygen is exhaled into the atmosphere."}
        ],
        "supported_learning_modes": ["Seeing", "Reading", "Listening"],
        "theme_tags": ["nature", "space", "science"],
        "icon_name": "Sun"
    },

    # NCERT CLASS 7 SCIENCE (CHAPTER 4): HEAT & TEMPERATURE
    {
        "title": "Cosmic Heat Conductor",
        "subject": "Science",
        "difficulty": 2,
        "estimated_duration": 5,
        "question": "When metal spoons sit in hot soup, heat travels from the hot soup through the spoon to the handle. What is this mode of heat transfer called in NCERT Science?",
        "content_type": "multiple_choice",
        "options": ["Conduction", "Convection", "Radiation", "Insulation"],
        "correct_answer": "Conduction",
        "explanation": "Conduction is the process where heat is transferred from the hotter end to the colder end of an object through direct molecular contact!",
        "hints": [
            "Heat moves through solid metals primarily by this process.",
            "It does not involve bulk movement of fluid like convection.",
            "The word sounds like 'conduct'."
        ],
        "steps": [
            {"step_number": 1, "title": "Hot End", "description": "Molecules in the spoon tip absorb thermal energy from soup.", "hint": "Molecules vibrate faster."},
            {"step_number": 2, "title": "Energy Pass", "description": "Molecules pass thermal kinetic energy to neighbor molecules.", "hint": "No fluid flow, just direct touch."},
            {"step_number": 3, "title": "Handle Warmth", "description": "Heat reaches your fingers via Conduction.", "hint": "Conduction transfers heat through solids."}
        ],
        "supported_learning_modes": ["Seeing", "Doing"],
        "theme_tags": ["science", "space", "general"],
        "icon_name": "Zap"
    },

    # NCERT CLASS 7 SCIENCE (CHAPTER 14): ELECTRIC CIRCUITS
    {
        "title": "Space Base Circuit Switch",
        "subject": "Science",
        "difficulty": 1,
        "estimated_duration": 4,
        "question": "To turn on the rover headlights, the electrical circuit must be complete without any breaks. What is a complete circuit called in NCERT Science?",
        "content_type": "multiple_choice",
        "options": ["Closed circuit", "Open circuit", "Short circuit", "Broken circuit"],
        "correct_answer": "Closed circuit",
        "explanation": "When the switch is in the 'ON' position, the electric circuit is complete from positive terminal to negative terminal, forming a closed circuit!",
        "hints": [
            "Think about whether the loop has any open gaps.",
            "Electricity only flows when the path is fully connected.",
            "It is the opposite of an 'open' circuit."
        ],
        "steps": [
            {"step_number": 1, "title": "Battery Connection", "description": "Current flows from the battery positive terminal.", "hint": "Power source active."},
            {"step_number": 2, "title": "Switch Position", "description": "Switch closes the metal contact gap.", "hint": "Bridge is down."},
            {"step_number": 3, "title": "Bulb Glow", "description": "Electricity returns to negative terminal in a closed circuit.", "hint": "Continuous loop = Closed circuit."}
        ],
        "supported_learning_modes": ["Seeing", "Doing"],
        "theme_tags": ["coding", "space", "science"],
        "icon_name": "Cpu"
    },

    # NCERT CLASS 7 MATHEMATICS (CHAPTER 1): INTEGERS
    {
        "title": "Sub-Zero Temperature Descent",
        "subject": "Mathematics",
        "difficulty": 1,
        "estimated_duration": 4,
        "question": "At base camp the temperature is 3°C. At midnight on the planetary ridge, the temperature drops by 8°C. What is the new temperature?",
        "content_type": "multiple_choice",
        "options": ["-5°C", "-11°C", "5°C", "-3°C"],
        "correct_answer": "-5°C",
        "explanation": "Starting at +3°C and dropping 8°C gives: 3 - 8 = -5°C!",
        "hints": [
            "Start on the number line at positive 3.",
            "Move 8 steps to the left toward negative numbers.",
            "3 - 3 reaches 0, and 5 more steps left reaches -5."
        ],
        "steps": [
            {"step_number": 1, "title": "Start at +3", "description": "Plot starting point 3 on the number line.", "hint": "+3 is right of 0."},
            {"step_number": 2, "title": "Step down to 0", "description": "Subtracting 3 drops temperature to 0°C.", "hint": "3 - 3 = 0."},
            {"step_number": 3, "title": "Below Zero", "description": "5 remaining steps left take you to -5°C.", "hint": "0 - 5 = -5°C."}
        ],
        "supported_learning_modes": ["Seeing", "Reading"],
        "theme_tags": ["space", "nature", "mathematics"],
        "icon_name": "Calculator"
    },

    # NCERT CLASS 7 MATHEMATICS (CHAPTER 2): FRACTIONS
    {
        "title": "Energy Cell Fraction",
        "subject": "Mathematics",
        "difficulty": 2,
        "estimated_duration": 4,
        "question": "A space shuttle power grid has 12 energy cells. If the navigation thrusters require 3/4 of the total cells, how many cells will be energized?",
        "content_type": "multiple_choice",
        "options": ["9 cells", "8 cells", "6 cells", "10 cells"],
        "correct_answer": "9 cells",
        "explanation": "(3/4) of 12 = (3 * 12) / 4 = 36 / 4 = 9 energy cells!",
        "hints": [
            "First find 1/4 of 12 by dividing 12 by 4.",
            "12 divided by 4 equals 3.",
            "Now multiply that answer (3) by 3 to find 3/4."
        ],
        "steps": [
            {"step_number": 1, "title": "Find One Fourth", "description": "Divide 12 total cells into 4 equal groups: 12 / 4 = 3.", "hint": "Each quarter is 3 cells."},
            {"step_number": 2, "title": "Take Three Quarters", "description": "Multiply 3 groups by 3: 3 * 3 = 9.", "hint": "3/4 of 12 = 9 cells."}
        ],
        "supported_learning_modes": ["Seeing", "Doing"],
        "theme_tags": ["space", "coding", "mathematics"],
        "icon_name": "Sparkles"
    },

    # NCERT CLASS 7 MATHEMATICS (CHAPTER 4): SIMPLE EQUATIONS
    {
        "title": "The Mystery Cargo Weight",
        "subject": "Mathematics",
        "difficulty": 2,
        "estimated_duration": 5,
        "question": "An expedition container holds 2 identical mystery probe pods plus a 5 kg sensor unit. The total weight on the scale is 25 kg. What is the weight of one mystery pod (x)?",
        "content_type": "multiple_choice",
        "options": ["10 kg", "12 kg", "8 kg", "15 kg"],
        "correct_answer": "10 kg",
        "explanation": "Equation: 2x + 5 = 25. Subtract 5: 2x = 20. Divide by 2: x = 10 kg!",
        "hints": [
            "Set up the balance: 2 pods + 5 kg = 25 kg.",
            "Subtract 5 kg from both sides to find what 2 pods weigh.",
            "20 kg divided equally into 2 pods equals 10 kg."
        ],
        "steps": [
            {"step_number": 1, "title": "Subtract the Constant", "description": "Remove 5 kg from both sides: 25 - 5 = 20 kg.", "hint": "2 pods = 20 kg."},
            {"step_number": 2, "title": "Isolate the Variable", "description": "Divide 20 kg by 2 pods: 20 / 2 = 10 kg.", "hint": "Each pod weighs 10 kg."}
        ],
        "supported_learning_modes": ["Seeing", "Reading"],
        "theme_tags": ["coding", "space", "mathematics"],
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
    
    # Upsert SEED_TASKS so all curriculum tasks (including newly added NCERT tasks) exist in MongoDB
    seeded_new = 0
    for task in SEED_TASKS:
        res = await db["tasks"].update_one(
            {"title": task["title"]},
            {"$set": task},
            upsert=True
        )
        if res.upserted_id:
            seeded_new += 1
    logger.info(f"Task synchronization complete: {len(SEED_TASKS)} base curriculum tasks checked ({seeded_new} newly created).")

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

    # Seed NCERT Knowledge Graph Concepts & Questions
    try:
        import os, json
        kg_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "curriculum", "ncert_knowledge_graph.json"))
        if os.path.exists(kg_path):
            with open(kg_path, "r", encoding="utf-8") as f:
                kg = json.load(f)
                import re
            for sub in kg.get("subjects", []):
                for ch in sub.get("chapters", []):
                    ch_id = ch.get("chapter_id", "")
                    g_match = re.search(r'_G(\d+)_', ch_id)
                    if g_match:
                        ch_grade = int(g_match.group(1))
                    else:
                        ch_grade = ch.get("grade") or sub.get("grade", 7)
                    ch_standard = ch.get("standard") or f"Class {ch_grade}"
                    for top in ch.get("topics", []):
                        for con in top.get("concepts", []):
                            await db["concepts"].update_one(
                                {"concept_id": con["concept_id"]},
                                {"$set": {
                                    "concept_id": con["concept_id"],
                                    "subject": sub["subject_name"],
                                    "grade": ch_grade,
                                    "standard": ch_standard,
                                    "chapter": ch["title"],
                                    "name": con["concept_name"],
                                    "learning_objectives": con.get("learning_objectives", []),
                                    "prerequisites": con.get("prerequisites", []),
                                    "explanation": con.get("explanation", {}),
                                    "misconceptions": con.get("common_misconceptions", [])
                                }},
                                upsert=True
                            )
                            for q in con.get("questions", []):
                                q_grade = q.get("grade") or ch_grade
                                q_standard = q.get("standard") or ch_standard
                                await db["tasks"].update_one(
                                    {"id": q["question_id"]},
                                    {"$set": {
                                        "id": q["question_id"],
                                        "concept_id": con["concept_id"],
                                        "title": f"{con['concept_name']} ({q.get('cognitive_level', 'RECALL')})",
                                        "subject": sub["subject_name"],
                                        "grade": q_grade,
                                        "standard": q_standard,
                                        "chapter": ch["title"],
                                        "difficulty": q.get("difficulty", 1),
                                        "question": q["prompt"],
                                        "options": q.get("options", []),
                                        "correct_answer": q["correct_answer"],
                                        "explanation": q.get("explanation", ""),
                                        "hints": q.get("hints", []),
                                        "scaffold_steps": q.get("scaffold_steps", []),
                                        "steps": [
                                            {
                                                "step_number": idx + 1,
                                                "title": s.split(":")[0].strip() if ":" in s else f"Step {idx + 1}",
                                                "description": s.split(":", 1)[1].strip() if ":" in s else s,
                                                "hint": None
                                            }
                                            for idx, s in enumerate(q.get("scaffold_steps", []))
                                        ],
                                        "cognitive_level": q.get("cognitive_level", "RECALL"),
                                        "supported_learning_modes": ["Seeing", "Doing"],
                                        "theme_tags": ["general", "space", "animals"]
                                    }},
                                    upsert=True
                                )
            logger.info("Successfully synced Multi-Standard NCERT Knowledge Graph concepts & tasks into MongoDB.")
    except Exception as e:
        logger.warning(f"Notice syncing knowledge graph: {e}")

    # Synchronize persistent students, drafts, and baseline profiles
    try:
        from app.services.student_store import load_persistent_students
        await load_persistent_students(db)
        logger.info("Successfully loaded persistent students and profiles.")
    except Exception as e:
        logger.warning(f"Notice loading persistent students: {e}")

