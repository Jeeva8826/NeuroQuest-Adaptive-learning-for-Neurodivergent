from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
from typing import List, Dict, Any, Optional
from bson import ObjectId

from app.database import get_database, SessionLocal
from app.services.auth_service import get_current_user
from app.models.schema import User as SqlUser, Learner as SqlLearner
from app.models.student import (
    StudentCreateInput,
    StudentUpdateInput,
    StudentResponse,
    Questionnaire20ResponseInput,
    QuestionnaireDraftInput,
    BaselineSupportProfile,
    BaselineSupportDimension
)
from app.models.learner_profile import LearnerProfile

router = APIRouter(prefix="/api/students", tags=["Students & Baseline Questionnaire"])

# ----------------------------------------------------
# 20-QUESTION EDUCATIONAL BASELINE QUESTIONNAIRE SCHEMA
# ----------------------------------------------------
QUESTIONNAIRE_20_SCHEMA = {
    "version": "baseline-v1",
    "title": "Student Learning Support & Personalization Baseline Questionnaire",
    "description": (
        "Constructs the student's initial educational support profile to configure "
        "sensory, pacing, scaffolding, and instruction preferences. Strictly non-diagnostic."
    ),
    "total_questions": 20,
    "disclaimer": (
        "This questionnaire is designed solely for educational personalization and baseline support planning. "
        "It is strictly non-diagnostic and does NOT evaluate, diagnose, or infer any medical condition. "
        "Observations do not replace assessment by a qualified healthcare or education professional."
    ),
    "questions": [
        {
            "id": "q1",
            "dimension": "attention_during_learning",
            "category": "Focus & Attention",
            "prompt": "How often does the student find it difficult to maintain attention during a standard learning activity?",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Sometimes"
        },
        {
            "id": "q2",
            "dimension": "maintaining_focus",
            "category": "Focus & Attention",
            "prompt": "When working on a learning task, how easily is the student drawn away by visual background movement or ambient activity?",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q3",
            "dimension": "task_initiation",
            "category": "Task Management",
            "prompt": "How often does the student experience hesitation or friction when getting started on a new learning activity?",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q4",
            "dimension": "task_completion",
            "category": "Task Management",
            "prompt": "How often does the student benefit from visual progress counters or checklists to see an activity through to completion?",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Very Often"
        },
        {
            "id": "q5",
            "dimension": "response_to_lengthy_instructions",
            "category": "Instruction Style",
            "prompt": "How challenging does the student find paragraphs with multiple instructions embedded together?",
            "type": "scale_difficulty",
            "scale_type": "difficulty_5",
            "options": ["Not challenging", "Slightly challenging", "Moderately challenging", "Very challenging", "Extremely challenging"],
            "default": "Very challenging"
        },
        {
            "id": "q6",
            "dimension": "preference_step_by_step",
            "category": "Instruction Style",
            "prompt": "How helpful is it for instructions to be presented as one single action per screen?",
            "type": "scale_helpfulness",
            "scale_type": "helpfulness_5",
            "options": ["Not helpful", "Slightly helpful", "Moderately helpful", "Very helpful", "Extremely helpful"],
            "default": "Extremely helpful"
        },
        {
            "id": "q7",
            "dimension": "preference_visual_explanations",
            "category": "Content Representation",
            "prompt": "How helpful are visual diagrams, illustrations, and infographics when understanding new concepts?",
            "type": "scale_helpfulness",
            "scale_type": "helpfulness_5",
            "options": ["Not helpful", "Slightly helpful", "Moderately helpful", "Very helpful", "Extremely helpful"],
            "default": "Extremely helpful"
        },
        {
            "id": "q8",
            "dimension": "preference_audio_explanations",
            "category": "Content Representation",
            "prompt": "How helpful is an on-demand audio read-aloud button (text-to-speech) during reading activities?",
            "type": "scale_helpfulness",
            "scale_type": "helpfulness_5",
            "options": ["Not helpful", "Slightly helpful", "Moderately helpful", "Very helpful", "Extremely helpful"],
            "default": "Very helpful"
        },
        {
            "id": "q9",
            "dimension": "reading_load_tolerance",
            "category": "Information Density",
            "prompt": "What volume of text does the student comfortably read on a single screen before fatigue sets in?",
            "type": "single_choice",
            "options": [
                "1 to 2 short sentences per card",
                "1 short paragraph (3 to 4 sentences)",
                "Standard book paragraphs",
                "Flexible long passages"
            ],
            "default": "1 to 2 short sentences per card"
        },
        {
            "id": "q10",
            "dimension": "response_information_dense_screens",
            "category": "Information Density",
            "prompt": "How often do crowded or visually busy screens cause the student visual discomfort or distraction?",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q11",
            "dimension": "changing_between_activities",
            "category": "Transitions & Flow",
            "prompt": "How helpful are transition countdowns or gentle cues when moving from one learning activity to another?",
            "type": "scale_helpfulness",
            "scale_type": "helpfulness_5",
            "options": ["Not helpful", "Slightly helpful", "Moderately helpful", "Very helpful", "Extremely helpful"],
            "default": "Very helpful"
        },
        {
            "id": "q12",
            "dimension": "response_repeated_practice",
            "category": "Practice & Reinforcement",
            "prompt": "How does the student best solidify a new concept through practice?",
            "type": "single_choice",
            "options": [
                "Fresh real-world analogies tied to interests",
                "Interactive visual puzzles & manipulatives",
                "Quick repeated micro-checks",
                "Independent open-ended exploration"
            ],
            "default": "Fresh real-world analogies tied to interests"
        },
        {
            "id": "q13",
            "dimension": "response_hints_scaffolding",
            "category": "Scaffolding & Support",
            "prompt": "When unsure of an answer, how helpful is an immediate, step-by-step hint ladder?",
            "type": "scale_helpfulness",
            "scale_type": "helpfulness_5",
            "options": ["Not helpful", "Slightly helpful", "Moderately helpful", "Very helpful", "Extremely helpful"],
            "default": "Extremely helpful"
        },
        {
            "id": "q14",
            "dimension": "preferred_learning_pace",
            "category": "Pacing & Timers",
            "prompt": "What learning pace allows the student to perform at their best?",
            "type": "single_choice",
            "options": [
                "Completely untimed, relaxed exploration",
                "Soft timer with optional pause/extension",
                "Moderately structured pace",
                "Fast-paced quick challenge"
            ],
            "default": "Completely untimed, relaxed exploration"
        },
        {
            "id": "q15",
            "dimension": "response_time_pressure",
            "category": "Pacing & Timers",
            "prompt": "How often do visible countdown clocks or ticking timers increase stress or performance anxiety for the student?",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q16",
            "dimension": "recovery_after_mistakes",
            "category": "Feedback & Resilience",
            "prompt": "When the student selects an incorrect answer, what feedback approach best supports their recovery and confidence?",
            "type": "single_choice",
            "options": [
                "Non-punitive gentle nudge with first step shown",
                "Positive encouraging retry prompt with no points lost",
                "Instant worked example without evaluation",
                "Silent retry allowing self-correction"
            ],
            "default": "Non-punitive gentle nudge with first step shown"
        },
        {
            "id": "q17",
            "dimension": "preferred_task_size",
            "category": "Task Granularity",
            "prompt": "What task unit size keeps the student most motivated and engaged?",
            "type": "single_choice",
            "options": [
                "Micro-challenges (1 to 2 minutes each)",
                "Bite-sized quests (3 to 5 minutes each)",
                "Moderate lessons (6 to 10 minutes)",
                "Extended project sessions (15+ minutes)"
            ],
            "default": "Micro-challenges (1 to 2 minutes each)"
        },
        {
            "id": "q18",
            "dimension": "preferred_feedback_style",
            "category": "Feedback & Resilience",
            "prompt": "Which style of achievement celebration feels most rewarding and non-overwhelming to the student?",
            "type": "single_choice",
            "options": [
                "Unlocking world components or space/cyber parts",
                "Gentle visual sparkles and quiet banner",
                "Quiet star counter with calm chime",
                "Enthusiastic celebratory sound and animation"
            ],
            "default": "Unlocking world components or space/cyber parts"
        },
        {
            "id": "q19",
            "dimension": "need_repetition_rephrasing",
            "category": "Instruction Style",
            "prompt": "How often does rephrasing a question using alternative vocabulary or visual metaphors help comprehension?",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q20",
            "dimension": "primary_support_benefit_area",
            "category": "Overall Focus Area",
            "prompt": "In which educational area does the student currently benefit from the greatest scaffolding and support?",
            "type": "single_choice",
            "options": [
                "Reading comprehension & dense text decoding",
                "Multi-step mathematical reasoning & word problems",
                "Conceptual science exploration with diagrams",
                "Task initiation, attention stamina & focus",
                "General stress-free confidence building"
            ],
            "default": "Task initiation, attention stamina & focus"
        }
    ]
}


# ----------------------------------------------------
# HELPER: Compute Educational Support Dimensions
# ----------------------------------------------------
def compute_baseline_support_dimensions(student_id: str, student_name: str, caretaker_id: str, responses: Dict[str, Any]) -> BaselineSupportProfile:
    """
    Computes 10 educational support dimensions from the 20 questions.
    STRICTLY NON-DIAGNOSTIC: Zero clinical cutoffs, probability scores, or DSM/ICD labels.
    """
    # 1. ATTENTION_SUPPORT (q1, q2)
    q1 = responses.get("q1", "Sometimes")
    q2 = responses.get("q2", "Often")
    attention_high = (q1 in ["Often", "Very Often"]) or (q2 in ["Often", "Very Often"])
    attention_support = "High Support (Distraction-Minimized)" if attention_high else "Moderate Support"

    # 2. INSTRUCTION_STYLE (q5, q6, q19)
    q5 = responses.get("q5", "Very challenging")
    q6 = responses.get("q6", "Extremely helpful")
    q19 = responses.get("q19", "Often")
    step_pref = (q6 in ["Very helpful", "Extremely helpful"]) or (q5 in ["Very challenging", "Extremely challenging"])
    instruction_style = "Sequential Step-by-Step (Single Action per Screen)" if step_pref else "Standard Structured Instructions"

    # 3. INFORMATION_DENSITY_SUPPORT (q9, q10)
    q9 = responses.get("q9", "1 to 2 short sentences per card")
    q10 = responses.get("q10", "Often")
    density_low = ("1 to 2" in q9) or (q10 in ["Often", "Very Often"])
    information_density = "Spacious Minimal Density" if density_low else "Balanced Standard Density"

    # 4. CONTENT_REPRESENTATION (q7, q8)
    q7 = responses.get("q7", "Extremely helpful")
    q8 = responses.get("q8", "Very helpful")
    visual_high = q7 in ["Very helpful", "Extremely helpful"]
    audio_high = q8 in ["Very helpful", "Extremely helpful"]
    if visual_high and audio_high:
        content_rep = "Multimodal (Visual Diagrams + Audio Read-Aloud)"
    elif visual_high:
        content_rep = "Visual Priority (Infographics & Diagrams)"
    elif audio_high:
        content_rep = "Auditory Priority (Text-to-Speech Enabled)"
    else:
        content_rep = "Standard Visual & Text"

    # 5. TASK_GRANULARITY (q17, q4)
    q17 = responses.get("q17", "Micro-challenges (1 to 2 minutes each)")
    task_small = ("Micro-challenges" in q17) or ("Bite-sized" in q17)
    task_granularity = "Micro-Challenges (1 to 2 min units)" if task_small else "Standard Challenge Units (3 to 5 mins)"

    # 6. PACE_SUPPORT (q14, q15)
    q14 = responses.get("q14", "Completely untimed, relaxed exploration")
    q15 = responses.get("q15", "Often")
    timer_sensitive = (q15 in ["Often", "Very Often"]) or ("untimed" in q14.lower())
    pace_support = "Completely Untimed Self-Directed Exploration" if timer_sensitive else "Gentle Soft-Timer with Unlimited Pause"

    # 7. SCAFFOLDING_SUPPORT (q13)
    q13 = responses.get("q13", "Extremely helpful")
    scaffold_high = q13 in ["Very helpful", "Extremely helpful"]
    scaffolding_support = "Continuous 7-Level Hint Ladder" if scaffold_high else "Standard Progressive Hints"

    # 8. FEEDBACK_SUPPORT (q16, q18)
    q16 = responses.get("q16", "Non-punitive gentle nudge with first step shown")
    feedback_support = f"Non-Punitive Recovery: {q16}"

    # 9. REPETITION_SUPPORT (q12)
    q12 = responses.get("q12", "Fresh real-world analogies tied to interests")
    repetition_support = f"Spiral Review: {q12}"

    # 10. TRANSITION_SUPPORT (q11, q3)
    q11 = responses.get("q11", "Very helpful")
    q3 = responses.get("q3", "Often")
    trans_needed = (q11 in ["Very helpful", "Extremely helpful"]) or (q3 in ["Often", "Very Often"])
    transition_support = "Gentle Countdown Cues & 1-Min Calming Breathers" if trans_needed else "Standard Smooth Transitions"

    # Recommended Accommodations Summary
    accommodations = [
        "High contrast, OpenDyslexic font typography option",
        "Spacious layout density with zero flashing/moving background elements",
        "Always-accessible text-to-speech audio reader button",
        "Untimed exploratory pacing without countdown anxiety",
        "Step-by-step hint ladder with positive, non-punitive retry feedback",
        "Sensory rest timers between learning milestones"
    ]

    # Initial UI Configuration
    initial_ui = {
        "visual_density": "spacious" if density_low else "balanced",
        "guidance_level": "high" if step_pref else "moderate",
        "task_size": "small" if task_small else "medium",
        "audio_mode": "on_demand" if audio_high else "standard",
        "animation_level": "none" if attention_high else "gentle",
        "calm_mode": True if timer_sensitive else False,
        "palette": "soft",
        "font_family": "OpenDyslexic"
    }

    # Structured dimensions list for rendering
    dimensions_list = [
        BaselineSupportDimension(
            dimension_key="ATTENTION_SUPPORT",
            title="Attention & Focus Support",
            support_level=attention_support,
            recommended_strategy="Minimize background animations; highlight active card with gentle contrast.",
            rationale="Reported sensitivity to visual movement or attention drift during multi-element screens."
        ),
        BaselineSupportDimension(
            dimension_key="INSTRUCTION_STYLE",
            title="Instruction Style & Guidance",
            support_level=instruction_style,
            recommended_strategy="Break multi-step prompts into single-clause, sequential cards.",
            rationale="Beneficial for reducing cognitive load when parsing complex requirements."
        ),
        BaselineSupportDimension(
            dimension_key="INFORMATION_DENSITY_SUPPORT",
            title="Information Density & Layout",
            support_level=information_density,
            recommended_strategy="Ample whitespace, large touch targets, single-concept focus per viewport.",
            rationale="Prevents visual fatigue and supports comfortable reading comprehension."
        ),
        BaselineSupportDimension(
            dimension_key="CONTENT_REPRESENTATION",
            title="Content Modality & Representation",
            support_level=content_rep,
            recommended_strategy="Pair diagrams and visual metaphors with optional audio narration.",
            rationale="Multimodal reinforcement supports deeper conceptual understanding."
        ),
        BaselineSupportDimension(
            dimension_key="TASK_GRANULARITY",
            title="Task Chunking & Granularity",
            support_level=task_granularity,
            recommended_strategy="Decompose curriculum objectives into 1-to-2 minute micro-quests.",
            rationale="Builds intrinsic motivation and momentum through frequent early milestones."
        ),
        BaselineSupportDimension(
            dimension_key="PACE_SUPPORT",
            title="Pacing & Time Pressure",
            support_level=pace_support,
            recommended_strategy="Remove visible clocks; allow learner full autonomy over completion pace.",
            rationale="Eliminates time-induced anxiety to foster thoughtful problem solving."
        ),
        BaselineSupportDimension(
            dimension_key="SCAFFOLDING_SUPPORT",
            title="Scaffolding & Hint Ladder",
            support_level=scaffolding_support,
            recommended_strategy="Provide on-demand 7-level scaffolding with partial step breakdowns.",
            rationale="Empowers independent recovery when encountering unfamiliar concepts."
        ),
        BaselineSupportDimension(
            dimension_key="FEEDBACK_SUPPORT",
            title="Feedback & Error Recovery",
            support_level=feedback_support,
            recommended_strategy="Employ gentle, non-punitive hints on incorrect attempts with zero lost stars.",
            rationale="Maintains emotional resilience and encourages safe exploratory risk-taking."
        ),
        BaselineSupportDimension(
            dimension_key="REPETITION_SUPPORT",
            title="Reinforcement & Spiral Review",
            support_level=repetition_support,
            recommended_strategy="Revisit core concepts using personalized interests (Space, Science, Robotics).",
            rationale="Grounds abstract principles in relatable, high-interest analogies."
        ),
        BaselineSupportDimension(
            dimension_key="TRANSITION_SUPPORT",
            title="Transitions & Sensory Balance",
            support_level=transition_support,
            recommended_strategy="Provide clear completion cues and optional 1-minute breathing checkpoints.",
            rationale="Supports smooth cognitive shifts between disparate subject areas."
        )
    ]

    return BaselineSupportProfile(
        student_id=student_id,
        student_name=student_name,
        caretaker_id=caretaker_id,
        version="baseline-v1",
        attention_support=attention_support,
        instruction_style=instruction_style,
        information_density_support=information_density,
        content_representation=content_rep,
        task_granularity=task_granularity,
        pace_support=pace_support,
        scaffolding_support=scaffolding_support,
        feedback_support=feedback_support,
        repetition_support=repetition_support,
        transition_support=transition_support,
        dimensions=dimensions_list,
        recommended_accommodations=accommodations,
        initial_ui_configuration=initial_ui,
        created_at=datetime.utcnow()
    )


# ----------------------------------------------------
# ENDPOINTS: Student CRUD & Ownership Validation
# ----------------------------------------------------
@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(
    student_in: StudentCreateInput,
    current_user: dict = Depends(get_current_user)
):
    """
    Caretaker registers a new student learner profile.
    Tied to authenticated caretaker ID.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))
    full_student_name = f"{student_in.first_name} {student_in.last_name}".strip()

    # 1. Persist to MongoDB learners collection
    student_doc = {
        "caretaker_id": caretaker_id,
        "first_name": student_in.first_name.strip(),
        "last_name": (student_in.last_name or "").strip(),
        "name": full_student_name,
        "age": student_in.age,
        "date_of_birth": student_in.date_of_birth,
        "grade": student_in.grade,
        "school_level": student_in.school_level,
        "school_name": student_in.school_name,
        "preferred_language": student_in.preferred_language,
        "interests": student_in.interests,
        "learning_environment": student_in.learning_environment,
        "preferred_communication": student_in.preferred_communication,
        "guardian_consent": student_in.guardian_consent,
        "has_completed_screening": False,
        "created_at": datetime.utcnow()
    }
    
    res = await db["learners"].insert_one(student_doc)
    student_id = str(res.inserted_id)

    # 2. Also record in SQL layer for relational integrity if SQL session exists
    try:
        if SessionLocal is not None:
            sql_session = SessionLocal()
            try:
                # Find user integer id if possible
                uid_int = int(caretaker_id) if caretaker_id.isdigit() else 1
                sql_learner = SqlLearner(
                    caregiver_id=uid_int,
                    name=full_student_name,
                    created_at=datetime.utcnow()
                )
                sql_session.add(sql_learner)
                sql_session.commit()
            finally:
                sql_session.close()
    except Exception:
        pass

    # 3. Update current user's active learner_id if none set
    await db["users"].update_many(
        {"$or": [{"_id": ObjectId(current_user["id"])} if ObjectId.is_valid(current_user["id"]) else {"id": current_user["id"]},
                 {"email": current_user.get("email")}]},
        {"$set": {"learner_id": student_id, "learner_name": full_student_name}}
    )

    return StudentResponse(
        id=student_id,
        caretaker_id=caretaker_id,
        first_name=student_in.first_name,
        name=full_student_name,
        age=student_in.age,
        grade=student_in.grade,
        school_level=student_in.school_level,
        preferred_language=student_in.preferred_language,
        interests=student_in.interests,
        has_completed_screening=False,
        created_at=student_doc["created_at"]
    )


@router.get("", response_model=List[StudentResponse])
async def list_caretaker_students(current_user: dict = Depends(get_current_user)):
    """
    Lists all students registered under the authenticated caretaker.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))
    
    # Query learners where caretaker_id matches user id or user email
    query = {"$or": [
        {"caretaker_id": caretaker_id},
        {"caregiver_id": caretaker_id},
        {"caretaker_email": current_user.get("email")}
    ]}
    
    cursor = db["learners"].find(query).sort("created_at", -1)
    learners = await cursor.to_list(length=50)

    result = []
    for l in learners:
        s_id = str(l.get("_id", l.get("id", "")))
        first_name = l.get("first_name") or l.get("name", "Student").split(" ")[0]
        result.append(StudentResponse(
            id=s_id,
            caretaker_id=str(l.get("caretaker_id", l.get("caregiver_id", caretaker_id))),
            first_name=first_name,
            name=l.get("name", first_name),
            age=l.get("age", 12),
            grade=l.get("grade", "Class 7"),
            school_level=l.get("school_level", "Middle School"),
            preferred_language=l.get("preferred_language", "English"),
            interests=l.get("interests", ["Science", "Space"]),
            has_completed_screening=bool(l.get("has_completed_screening", False)),
            created_at=l.get("created_at", datetime.utcnow())
        ))
    return result


@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(
    student_id: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Fetches a specific student with ownership validation.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))

    # Validate ObjectId or string ID
    query = {"_id": ObjectId(student_id)} if ObjectId.is_valid(student_id) else {"id": student_id}
    student = await db["learners"].find_one(query)
    
    if not student:
        raise HTTPException(status_code=404, detail="Student record not found.")

    # Authorization verification: caretaker must own the student
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    if student_caretaker and student_caretaker != caretaker_id and current_user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized access: You do not have permission to view this student.")

    first_name = student.get("first_name") or student.get("name", "Student").split(" ")[0]
    return StudentResponse(
        id=str(student.get("_id", student_id)),
        caretaker_id=student_caretaker or caretaker_id,
        first_name=first_name,
        name=student.get("name", first_name),
        age=student.get("age", 12),
        grade=student.get("grade", "Class 7"),
        school_level=student.get("school_level", "Middle School"),
        preferred_language=student.get("preferred_language", "English"),
        interests=student.get("interests", ["Science", "Space"]),
        has_completed_screening=bool(student.get("has_completed_screening", False)),
        created_at=student.get("created_at", datetime.utcnow())
    )


# ----------------------------------------------------
# ENDPOINTS: 20-Question Questionnaire & Draft Flow
# ----------------------------------------------------
@router.get("/{student_id}/questionnaire")
async def get_student_questionnaire(
    student_id: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Returns the 20-question questionnaire schema and any saved draft for the student.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))

    # Verify student ownership
    query = {"_id": ObjectId(student_id)} if ObjectId.is_valid(student_id) else {"id": student_id}
    student = await db["learners"].find_one(query)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    if student_caretaker and student_caretaker != caretaker_id and current_user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    # Retrieve draft if exists
    draft_doc = await db["questionnaire_drafts"].find_one({"student_id": student_id})
    draft_data = {
        "responses": draft_doc.get("responses", {}) if draft_doc else {},
        "current_question": draft_doc.get("current_question", 1) if draft_doc else 1
    }

    return {
        "schema": QUESTIONNAIRE_20_SCHEMA,
        "student": {
            "id": student_id,
            "name": student.get("name", "Student"),
            "first_name": student.get("first_name", student.get("name", "Student")),
            "age": student.get("age", 12),
            "grade": student.get("grade", "Class 7")
        },
        "draft": draft_data
    }


@router.post("/{student_id}/questionnaire/draft")
async def save_questionnaire_draft(
    student_id: str,
    draft: QuestionnaireDraftInput,
    current_user: dict = Depends(get_current_user)
):
    """
    Saves in-progress questionnaire responses so progress survives page refresh.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))

    # Verify student ownership
    query = {"_id": ObjectId(student_id)} if ObjectId.is_valid(student_id) else {"id": student_id}
    student = await db["learners"].find_one(query)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    if student_caretaker and student_caretaker != caretaker_id and current_user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    await db["questionnaire_drafts"].update_one(
        {"student_id": student_id},
        {
            "$set": {
                "student_id": student_id,
                "caretaker_id": caretaker_id,
                "responses": draft.responses,
                "current_question": draft.current_question,
                "updated_at": datetime.utcnow()
            }
        },
        upsert=True
    )
    return {"message": "Draft saved successfully", "saved_at": datetime.utcnow()}


@router.post("/{student_id}/questionnaire/complete", response_model=BaselineSupportProfile)
async def complete_student_questionnaire(
    student_id: str,
    submission: Questionnaire20ResponseInput,
    current_user: dict = Depends(get_current_user)
):
    """
    Submits all 20 questions, computes 10 non-diagnostic educational support dimensions,
    stores baseline support profile, and seeds runtime LearnerProfile for NeuroQuest.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))

    # Verify student ownership
    query = {"_id": ObjectId(student_id)} if ObjectId.is_valid(student_id) else {"id": student_id}
    student = await db["learners"].find_one(query)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    if student_caretaker and student_caretaker != caretaker_id and current_user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    student_name = student.get("name", "Student")
    responses = submission.responses

    # 1. Compute 10 Educational Support Dimensions (Strictly non-diagnostic)
    profile = compute_baseline_support_dimensions(
        student_id=student_id,
        student_name=student_name,
        caretaker_id=caretaker_id,
        responses=responses
    )

    # 2. Persist baseline support profile in MongoDB
    profile_dict = profile.model_dump()
    await db["baseline_support_profiles"].update_one(
        {"student_id": student_id},
        {"$set": profile_dict},
        upsert=True
    )

    # 3. Mark student as completed screening
    await db["learners"].update_one(
        query,
        {"$set": {
            "has_completed_screening": True,
            "screening_completed_at": datetime.utcnow()
        }}
    )

    # 4. Initialize or update runtime LearnerProfile state for NeuroQuest engine
    interests = student.get("interests", ["Science", "Space"])
    runtime_profile = {
        "learner_id": student_id,
        "caregiver_id": caretaker_id,
        "learner_name": student_name,
        "learner_age": student.get("age", 12),
        "interests": interests,
        "visual_preferences": {
            "primary_color": "#2563EB",
            "secondary_color": "#38BDF8",
            "palette_type": "soft",
            "background_theme": "space",
            "font_family": "OpenDyslexic",
            "font_scale": "medium"
        },
        "sensory_preferences": {
            "sound_enabled": True,
            "sound_preference": "quiet",
            "animation_intensity": "none" if "High Support" in profile.attention_support else "gentle",
            "visual_density": "spacious" if "Spacious" in profile.information_density_support else "balanced",
            "calm_mode": True
        },
        "interaction_preferences": {
            "task_size": "small" if "Micro-Challenges" in profile.task_granularity else "medium",
            "guidance_level": "high" if "Sequential" in profile.instruction_style else "moderate",
            "feedback_style": "immediate",
            "break_frequency_mins": 5 if "Breathers" in profile.transition_support else 10
        },
        "gamification": {
            "motivation_types": ["exploration", "collection"],
            "game_theme": "space",
            "reward_preference": "unlockables",
            "interaction_preference": "step_by_step",
            "celebration_preference": "gentle_sparkles",
            "progress_style": "mastery_tree"
        },
        "updated_at": datetime.utcnow()
    }
    
    await db["learner_preferences"].update_one(
        {"learner_id": student_id},
        {"$set": runtime_profile},
        upsert=True
    )

    # Also set active learner for caretaker user
    await db["users"].update_many(
        {"$or": [{"_id": ObjectId(current_user["id"])} if ObjectId.is_valid(current_user["id"]) else {"id": current_user["id"]},
                 {"email": current_user.get("email")}]},
        {"$set": {"learner_id": student_id, "learner_name": student_name}}
    )

    # 5. Clean up draft
    await db["questionnaire_drafts"].delete_one({"student_id": student_id})

    return profile


@router.get("/{student_id}/baseline-profile", response_model=BaselineSupportProfile)
async def get_student_baseline_profile(
    student_id: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Retrieves the computed non-diagnostic baseline support profile for a student.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))

    # Verify student ownership
    query = {"_id": ObjectId(student_id)} if ObjectId.is_valid(student_id) else {"id": student_id}
    student = await db["learners"].find_one(query)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    if student_caretaker and student_caretaker != caretaker_id and current_user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    profile_doc = await db["baseline_support_profiles"].find_one({"student_id": student_id})
    if not profile_doc:
        raise HTTPException(
            status_code=404,
            detail="Baseline support profile not found. Please complete the 20-question questionnaire first."
        )

    return BaselineSupportProfile(**profile_doc)
