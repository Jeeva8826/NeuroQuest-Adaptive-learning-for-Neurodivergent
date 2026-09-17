import json
import os

SCHEMA_FIELDS = [
    "grade", "subject", "chapter", "concept_id", "learning_objective", 
    "difficulty", "question_type", "representation", "prompt", "options", 
    "answer", "explanation", "hint_ladder", "prerequisites", "cognitive_load", 
    "accessibility_variants", "source"
]

def create_question(grade, subject, chapter, concept_id, learning_objective, difficulty, question_type, representation, prompt, options, answer, explanation, hint_ladder, prerequisites, cognitive_load, accessibility_variants, source):
    return {
        "grade": grade,
        "subject": subject,
        "chapter": chapter,
        "concept_id": concept_id,
        "learning_objective": learning_objective,
        "difficulty": difficulty,
        "question_type": question_type,
        "representation": representation,
        "prompt": prompt,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "hint_ladder": hint_ladder,
        "prerequisites": prerequisites,
        "cognitive_load": cognitive_load,
        "accessibility_variants": accessibility_variants,
        "source": source
    }

questions = []

# Question 1: Recognition (Level 1)
q1_accessibility_variants = {
    "chunked": {
        "prompt": "Plants make their own food.\nThey use a special process.\nWhat is the name of this process?",
        "options": ["Respiration", "Photosynthesis", "Digestion", "Transpiration"]
    },
    "visual": {
        "prompt": "Look at the image showing a plant absorbing sunlight, water, and carbon dioxide to make food. What is this process called?",
        "image_url": "assets/images/photosynthesis_basic.png",
        "options": ["Respiration", "Photosynthesis", "Digestion", "Transpiration"]
    },
    "scaffolded": {
        "prompt": "Plants need sunlight to make food. The word for this process starts with 'Photo' (meaning light). What is the full name of the process?",
        "options": ["Photosynthesis", "Phototropism", "Photography", "Photocell"]
    }
}

q1 = create_question(
    grade=7,
    subject="Science",
    chapter="Nutrition in Plants",
    concept_id="BIO_7_01_01",
    learning_objective="Recall the name of the food-making process in plants.",
    difficulty=1,
    question_type="multiple_choice",
    representation="text",
    prompt="What is the process by which green plants make their own food called?",
    options=["Respiration", "Photosynthesis", "Digestion", "Transpiration"],
    answer="Photosynthesis",
    explanation="Photosynthesis is the process by which green plants use sunlight, water, and carbon dioxide to synthesize food.",
    hint_ladder=[
        "It involves light.",
        "The prefix 'photo' means light."
    ],
    prerequisites=["Plants are living things", "Plants need food"],
    cognitive_load="Low",
    accessibility_variants=q1_accessibility_variants,
    source="NCERT Class 7 Science Chapter 1"
)
questions.append(q1)

# Question 2: Understanding (Level 2)
q2_accessibility_variants = {
    "chunked": {
        "prompt": "Photosynthesis requires a few key things.\nWhich of the following is NOT required for photosynthesis to occur?",
        "options": ["Sunlight", "Carbon dioxide", "Oxygen", "Water"]
    },
    "choice-based": {
        "prompt": "Choose the gas that plants release, NOT the one they take in for photosynthesis.",
        "options": ["Oxygen", "Carbon dioxide", "Nitrogen"]
    }
}

q2 = create_question(
    grade=7,
    subject="Science",
    chapter="Nutrition in Plants",
    concept_id="BIO_7_01_02",
    learning_objective="Identify the essential components required for photosynthesis.",
    difficulty=2,
    question_type="multiple_choice",
    representation="text",
    prompt="Which of the following is NOT required by plants to carry out photosynthesis?",
    options=["Sunlight", "Carbon dioxide", "Oxygen", "Water"],
    answer="Oxygen",
    explanation="Plants require sunlight, carbon dioxide, and water for photosynthesis. They produce oxygen as a byproduct, they do not require it for the process.",
    hint_ladder=[
        "Think about what plants take in from the air and soil.",
        "Plants give out this gas, humans breathe it in."
    ],
    prerequisites=["Photosynthesis definition"],
    cognitive_load="Medium",
    accessibility_variants=q2_accessibility_variants,
    source="NCERT Class 7 Science Chapter 1"
)
questions.append(q2)

# Question 3: Application (Level 3)
q3_accessibility_variants = {
    "scaffolded": {
        "prompt": "Step 1: Leaves are the food factories of plants.\nStep 2: A plant with no leaves cannot make food.\nWhat will happen to a plant if all its leaves are removed?",
        "options": ["It will die", "It will grow faster", "It will grow new roots"]
    }
}

q3 = create_question(
    grade=7,
    subject="Science",
    chapter="Nutrition in Plants",
    concept_id="BIO_7_01_03",
    learning_objective="Apply the concept of photosynthesis to real-world scenarios regarding plant survival.",
    difficulty=3,
    question_type="multiple_choice",
    representation="text",
    prompt="If a plant is kept in a dark room for a long time, it will eventually die. What is the primary reason for this?",
    options=[
        "It cannot absorb water from the soil.",
        "It cannot perform photosynthesis to produce food.",
        "It does not get enough oxygen to breathe.",
        "It is attacked by pests in the dark."
    ],
    answer="It cannot perform photosynthesis to produce food.",
    explanation="Without sunlight, the plant cannot carry out photosynthesis to make its food. Without food, it runs out of energy and dies.",
    hint_ladder=[
        "What is the main source of energy for the plant?",
        "How does a plant make its food?",
        "Sunlight is necessary for photosynthesis."
    ],
    prerequisites=["Photosynthesis requirements"],
    cognitive_load="High",
    accessibility_variants=q3_accessibility_variants,
    source="NCERT Class 7 Science Chapter 1"
)
questions.append(q3)

# Question 4: Reasoning (Level 4)
q4_accessibility_variants = {
    "chunked": {
        "prompt": "Leaves have a green pigment.\nIt helps capture sunlight.\nSome plants have red or brown leaves.\nCan they still perform photosynthesis?\nWhy?",
        "options": ["Yes, they have hidden green pigment", "No, they don't have green pigment"]
    }
}

q4 = create_question(
    grade=7,
    subject="Science",
    chapter="Nutrition in Plants",
    concept_id="BIO_7_01_04",
    learning_objective="Analyze and reason about atypical cases of photosynthesis.",
    difficulty=4,
    question_type="multiple_choice",
    representation="text",
    prompt="Some plants have deep red, violet, or brown leaves. Do these leaves also carry out photosynthesis? Why or why not?",
    options=[
        "No, because they lack chlorophyll.",
        "Yes, the red, brown, and other pigments mask the green color of chlorophyll.",
        "No, they absorb food from other plants.",
        "Yes, they use red pigments instead of chlorophyll to trap sunlight."
    ],
    answer="Yes, the red, brown, and other pigments mask the green color of chlorophyll.",
    explanation="These leaves do contain chlorophyll. The large amount of red, brown and other pigments mask the green colour. Photosynthesis takes place in these leaves also.",
    hint_ladder=[
        "Chlorophyll is necessary for photosynthesis.",
        "Can chlorophyll be present but not visible?"
    ],
    prerequisites=["Role of chlorophyll in photosynthesis"],
    cognitive_load="Very High",
    accessibility_variants=q4_accessibility_variants,
    source="NCERT Class 7 Science Chapter 1"
)
questions.append(q4)


# Ensure output directory exists
output_dir = "../../data/questions/ncert_aligned"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "photosynthesis_questions.json")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=4)

print(f"Successfully generated {len(questions)} questions in {output_file}")
