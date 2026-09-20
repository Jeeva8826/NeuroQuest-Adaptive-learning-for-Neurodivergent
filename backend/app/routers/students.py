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
from app.services.student_store import (
    find_or_recover_student, save_persistent_students, load_persistent_students
)

router = APIRouter(prefix="/api/students", tags=["Students & Baseline Questionnaire"])

# ----------------------------------------------------
# 20-QUESTION EDUCATIONAL BASELINE QUESTIONNAIRE SCHEMA
# ----------------------------------------------------
QUESTIONNAIRE_20_SCHEMA = {
    "version": "baseline-v2-dataset-aligned",
    "title": "Student Educational Support & Personalized Learning Assessment",
    "description": (
        "Constructs the student's individualized learning support profile strictly from "
        "observable educational accessibility dimensions (Sensory processing preferences, executive function scaffolding, "
        "reading & decoding support, pacing, and task chunking) to configure sensory modes, typography, and hints."
    ),
    "total_questions": 20,
    "disclaimer": (
        "This questionnaire analyzes student educational and sensory preferences solely for educational personalization "
        "and baseline accessibility planning. It is strictly non-diagnostic, contains zero medical fields or diagnostic labels, "
        "and does not replace a comprehensive clinical diagnosis by a qualified healthcare professional."
    ),
    "questions": [
        {
            "id": "q1",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A1)",
            "dimension": "auditory_sensitivity",
            "category": "Sensory Processing (AQ-10 A1)",
            "prompt": "How often does the student notice small sounds or subtle background hums that others do not notice?",
            "personalization_impact": "Calibrates sound dampening, eliminates harsh audio alerts, and enables calm chime feedback.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q2",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A2)",
            "dimension": "detail_vs_global_focus",
            "category": "Cognitive Processing (AQ-10 A2)",
            "prompt": "Does the student concentrate more intensely on small concrete details rather than the big picture?",
            "personalization_impact": "Orders challenge prompts into an atomic step-by-step ladder before presenting abstract conclusions.",
            "type": "scale_agreement",
            "scale_type": "agreement_4",
            "options": ["Definitely Disagree", "Slightly Disagree", "Slightly Agree", "Definitely Agree"],
            "default": "Definitely Agree"
        },
        {
            "id": "q3",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A3)",
            "dimension": "multi_stream_filtering",
            "category": "Sensory & Auditory Filtering (AQ-10 A3)",
            "prompt": "When in a group or noisy setting, how challenging is it for the student to keep track of a conversation?",
            "personalization_impact": "Enforces isolated single-stream audio narration; never plays background sound over text prompts.",
            "type": "scale_difficulty",
            "scale_type": "difficulty_5",
            "options": ["Not challenging", "Slightly challenging", "Moderately challenging", "Very challenging", "Extremely challenging"],
            "default": "Very challenging"
        },
        {
            "id": "q4",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A4)",
            "dimension": "cognitive_flexibility_transitions",
            "category": "Executive Function & Transitions (AQ-10 A4)",
            "prompt": "How challenging does the student find it to transition or switch back and forth between different activities?",
            "personalization_impact": "Activates transition countdown cues, visual task completion roadmaps, and 1-minute calming breathers.",
            "type": "scale_difficulty",
            "scale_type": "difficulty_5",
            "options": ["Not challenging", "Slightly challenging", "Moderately challenging", "Very challenging", "Extremely challenging"],
            "default": "Very challenging"
        },
        {
            "id": "q5",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A5)",
            "dimension": "reciprocal_communication",
            "category": "Social & Communication Style (AQ-10 A5)",
            "prompt": "How often does the student experience difficulty maintaining spontaneous, multi-turn conversation flow with peers?",
            "personalization_impact": "Formats learning companion dialogues into direct, structured, and predictable guidance cards.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q6",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A6)",
            "dimension": "pragmatic_language",
            "category": "Language & Phrasing Style (AQ-10 A6)",
            "prompt": "Does the student find casual social chit-chat or informal conversational slang confusing or unengaging?",
            "personalization_impact": "Removes ambiguous idioms; delivers instructions using clear, literal, and unambiguous language.",
            "type": "scale_agreement",
            "scale_type": "agreement_4",
            "options": ["Definitely Disagree", "Slightly Disagree", "Slightly Agree", "Definitely Agree"],
            "default": "Slightly Agree"
        },
        {
            "id": "q7",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A7)",
            "dimension": "contextual_inference_theory_of_mind",
            "category": "Narrative & Reading Processing (AQ-10 A7)",
            "prompt": "When reading a story or scenario, how difficult is it for the student to infer character intentions or emotional subtext?",
            "personalization_impact": "Anchors questions with explicit real-world interest analogies (Space, Animals, Robotics) instead of abstract drama.",
            "type": "scale_difficulty",
            "scale_type": "difficulty_5",
            "options": ["Not difficult", "Slightly difficult", "Moderately difficult", "Very difficult", "Extremely difficult"],
            "default": "Very difficult"
        },
        {
            "id": "q8",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A8)",
            "dimension": "concrete_vs_abstract_logic",
            "category": "Reasoning & Representation (AQ-10 A8)",
            "prompt": "Does the student strongly prefer concrete, predictable, and rule-based tasks over open-ended pretend play?",
            "personalization_impact": "Selects structured interactive logic puzzles and visual manipulatives over open-ended speculation.",
            "type": "scale_agreement",
            "scale_type": "agreement_4",
            "options": ["Definitely Disagree", "Slightly Disagree", "Slightly Agree", "Definitely Agree"],
            "default": "Definitely Agree"
        },
        {
            "id": "q9",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A9)",
            "dimension": "visual_social_cues",
            "category": "Visual Processing (AQ-10 A9)",
            "prompt": "Does the student find it difficult to interpret feelings or intent purely from human facial expressions?",
            "personalization_impact": "Replaces human facial feedback avatars with calm, supportive symbolic icons (Stars, Sparkles, Compass).",
            "type": "scale_agreement",
            "scale_type": "agreement_4",
            "options": ["Definitely Disagree", "Slightly Disagree", "Slightly Agree", "Definitely Agree"],
            "default": "Definitely Agree"
        },
        {
            "id": "q10",
            "dataset_source": "Kaggle Autism_Child_Data.csv (Item A10)",
            "dimension": "peer_social_interaction",
            "category": "Social & Learning Environment (AQ-10 A10)",
            "prompt": "How often does the student feel overwhelmed or anxious when participating in peer group social settings?",
            "personalization_impact": "Locks experience into a private, self-paced mastery environment; disables public leaderboards.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q11",
            "dataset_source": "Kaggle Autism_Child_Data.csv (jundice column)",
            "dimension": "early_developmental_jaundice",
            "category": "Medical & Developmental Background",
            "prompt": "Did the student experience neonatal jaundice or early sensory processing sensitivities in infancy?",
            "personalization_impact": "Calibrates conservative sensory thresholds to safeguard against early visual and auditory fatigue.",
            "type": "single_choice",
            "options": ["Yes - Documented history", "No - Typical developmental course", "Unsure / Prefer not to specify"],
            "default": "No - Typical developmental course"
        },
        {
            "id": "q12",
            "dataset_source": "Kaggle Autism_Child_Data.csv (austim column)",
            "dimension": "family_neurodivergence_history",
            "category": "Medical & Developmental Background",
            "prompt": "Is there a documented personal or family history of autism, ADHD, dyslexia, or executive processing differences?",
            "personalization_impact": "Activates the multimodal neurodivergent accommodation baseline (visual + audio + hint ladder).",
            "type": "single_choice",
            "options": [
                "Yes - Confirmed diagnosis or strong family traits",
                "Under formal evaluation",
                "No documented history",
                "Prefer not to specify"
            ],
            "default": "Yes - Confirmed diagnosis or strong family traits"
        },
        {
            "id": "q13",
            "dataset_source": "Clinical ADHD Screening (medical_service.py Item 2)",
            "dimension": "attention_stamina_distraction",
            "category": "Attention & Focus Stamina",
            "prompt": "How often does the student experience difficulty sustaining attention throughout a standard learning challenge?",
            "personalization_impact": "Activates Focus Mode (dims background distraction, spotlights active question card).",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q14",
            "dataset_source": "Clinical ADHD Screening (medical_service.py Item 8)",
            "dimension": "extraneous_visual_movement",
            "category": "Sensory Distractibility",
            "prompt": "When working on a screen, how easily is the student drawn away by extraneous background movement or blinking graphics?",
            "personalization_impact": "Sets Visual Density to Spacious Minimal; permanently disables background animations.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q15",
            "dataset_source": "Clinical ADHD Screening (medical_service.py Item 6)",
            "dimension": "task_initiation_hesitation",
            "category": "Executive Function & Initiation",
            "prompt": "How often does the student avoid or hesitate to get started on tasks that require sustained mental effort?",
            "personalization_impact": "Deploys 'First Step Helper' offering an instant breakdown with the first clue pre-highlighted.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q16",
            "dataset_source": "Clinical Sensory Assessment (medical_service.py Item 20)",
            "dimension": "photophobia_glare_sensitivity",
            "category": "Visual Sensory Processing",
            "prompt": "Does the student show discomfort, squinting, or fatigue from bright stark white screens or high visual glare?",
            "personalization_impact": "Auto-selects Calm Mode with soft warm pastel tones and low luminance.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q17",
            "dataset_source": "Clinical Dyslexia Assessment (medical_service.py Item 6)",
            "dimension": "letter_confusion_crowding",
            "category": "Visual Decoding & Dyslexia",
            "prompt": "Does the student confuse visually similar letters (such as b/d, p/q) or struggle when text lines are crowded?",
            "personalization_impact": "Enforces OpenDyslexic font typography, increased letter tracking, and generous line spacing.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q18",
            "dataset_source": "Clinical Dyslexia Assessment (medical_service.py Item 4)",
            "dimension": "text_to_speech_read_aloud",
            "category": "Modality & Auditory Support",
            "prompt": "How helpful is having an on-demand audio read-aloud button (text-to-speech) during reading activities?",
            "personalization_impact": "Pins prominent speech narration buttons on every question and hint ladder.",
            "type": "scale_helpfulness",
            "scale_type": "helpfulness_5",
            "options": ["Not helpful", "Slightly helpful", "Moderately helpful", "Very helpful", "Extremely helpful"],
            "default": "Extremely helpful"
        },
        {
            "id": "q19",
            "dataset_source": "WALS Neurodivergent Learner Dataset (Timer Anxiety Benchmark)",
            "dimension": "timer_anxiety_pacing",
            "category": "Pacing & Pressure",
            "prompt": "How often do visible countdown clocks, ticking timers, or speed limits increase stress or cause rushed mistakes?",
            "personalization_impact": "Removes all countdown clocks completely; enables untimed self-directed exploratory pacing.",
            "type": "scale_frequency",
            "scale_type": "frequency_5",
            "options": ["Never", "Rarely", "Sometimes", "Often", "Very Often"],
            "default": "Often"
        },
        {
            "id": "q20",
            "dataset_source": "WALS Neurodivergent Learner Dataset & Resilience Metrics",
            "dimension": "error_recovery_feedback_style",
            "category": "Feedback & Emotional Resilience",
            "prompt": "When an answer is incorrect, what feedback approach best supports recovery and emotional resilience?",
            "personalization_impact": "Enforces non-punitive recovery: zero star loss, gentle step hint shown, safe instant retry.",
            "type": "single_choice",
            "options": [
                "Non-punitive gentle nudge with first step shown",
                "Positive encouraging retry prompt with no points lost",
                "Instant worked example without evaluation",
                "Silent retry allowing self-correction"
            ],
            "default": "Non-punitive gentle nudge with first step shown"
        }
    ]
}


# ----------------------------------------------------
# HELPER: Compute Educational Support Dimensions & Domain Indices
# ----------------------------------------------------
def compute_baseline_support_dimensions(student_id: str, student_name: str, caretaker_id: str, responses: Dict[str, Any]) -> BaselineSupportProfile:
    """
    Computes 10 educational support dimensions and 5 pedagogical support domain indices
    from the 20 questions grounded in accessibility and universal design for learning (UDL) frameworks.
    STRICTLY NON-DIAGNOSTIC: Translates observable learning preferences into accessibility adaptations.
    Contains zero medical or diagnostic labels.
    """
    def is_high(val, keys=("often", "very often", "extremely", "very helpful", "definitely agree", "yes")):
        s = str(val).lower()
        return any(k in s for k in keys)

    # Extract all 20 responses upfront with sensible defaults
    q1 = responses.get("q1", "Often")
    q2 = responses.get("q2", "Definitely Agree")
    q3 = responses.get("q3", "Very challenging")
    q4 = responses.get("q4", "Very challenging")
    q5 = responses.get("q5", "Often")
    q6 = responses.get("q6", "Slightly Agree")
    q7 = responses.get("q7", "Slightly Agree")
    q8 = responses.get("q8", "Definitely Agree")
    q9 = responses.get("q9", "Definitely Agree")
    q10 = responses.get("q10", "Often")
    q11 = responses.get("q11", "No - Typical developmental course")
    q12 = responses.get("q12", "Yes - Confirmed diagnosis or strong family traits")
    q13 = responses.get("q13", "Often")
    q14 = responses.get("q14", "Often")
    q15 = responses.get("q15", "Often")
    q16 = responses.get("q16", "Often")
    q17 = responses.get("q17", "Often")
    q18 = responses.get("q18", "Extremely helpful")
    q19 = responses.get("q19", "Often")
    q20 = responses.get("q20", "Non-punitive gentle nudge with first step shown")

    # 1. ATTENTION_SUPPORT (q13 attention stamina, q14 visual movement)
    attention_high = is_high(q13) or is_high(q14)
    attention_support = "High Support (Distraction-Minimized)" if attention_high else "Moderate Support"

    # 2. INSTRUCTION_STYLE (q2 detail focus, q6 literal phrasing, q15 initiation)
    step_pref = is_high(q2) or is_high(q15) or is_high(q6)
    instruction_style = "Sequential Step-by-Step (Single Action per Screen)" if step_pref else "Standard Structured Instructions"

    # 3. INFORMATION_DENSITY_SUPPORT (q14 visual clutter, q16 glare, q17 letter crowding)
    density_low = is_high(q14) or is_high(q16) or is_high(q17)
    information_density = "Spacious Minimal Density" if density_low else "Balanced Standard Density"

    # 4. CONTENT_REPRESENTATION (q8 concrete logic, q18 read-aloud)
    visual_high = is_high(q8)
    audio_high = is_high(q18)
    if visual_high and audio_high:
        content_rep = "Multimodal (Visual Diagrams + Audio Read-Aloud)"
    elif visual_high:
        content_rep = "Visual Priority (Infographics & Diagrams)"
    elif audio_high:
        content_rep = "Auditory Priority (Text-to-Speech Enabled)"
    else:
        content_rep = "Standard Visual & Text"

    # 5. TASK_GRANULARITY (q4 task switching, q15 initiation)
    task_small = is_high(q4) or is_high(q15)
    task_granularity = "Micro-Challenges (1 to 2 min units)" if task_small else "Standard Challenge Units (3 to 5 mins)"

    # 6. PACE_SUPPORT (q19 timer anxiety)
    timer_sensitive = is_high(q19)
    pace_support = "Completely Untimed Self-Directed Exploration" if timer_sensitive else "Gentle Soft-Timer with Unlimited Pause"

    # 7. SCAFFOLDING_SUPPORT (q2 detail focus, q15 task initiation)
    scaffold_high = is_high(q2) or is_high(q15)
    scaffolding_support = "Continuous 7-Level Hint Ladder" if scaffold_high else "Standard Progressive Hints"

    # 8. FEEDBACK_SUPPORT (q20 recovery feedback)
    feedback_support = f"Non-Punitive Recovery: {q20}"

    # 9. REPETITION_SUPPORT (q7 story inference, interest analogies)
    repetition_support = "Spiral Review: Fresh real-world analogies tied to interests"

    # 10. TRANSITION_SUPPORT (q4 activity transitions, q10 peer social friction)
    trans_needed = is_high(q4) or is_high(q10)
    transition_support = "Gentle Countdown Cues & 1-Min Calming Breathers" if trans_needed else "Standard Smooth Transitions"

    # 5 Pedagogical Support Dimension Indices (Strictly Non-Diagnostic)
    sensory_score = sum([is_high(q1), is_high(q3), is_high(q14), is_high(q16)])
    flexibility_score = sum([is_high(q4), is_high(q5), is_high(q15)])
    reading_score = sum([is_high(q7), is_high(q17), is_high(q18)])
    attention_score = sum([is_high(q2), is_high(q13), is_high(q19)])

    clinical_domain_indices = {
        "sensory_reactivity_index": {
            "score": f"{sensory_score}/4",
            "level": "Sensory Environment Customization Needed" if sensory_score >= 2 else "Standard Sensory Setting",
            "items_analyzed": ["Acoustic Sensitivity Indicator", "Background Sound Level Preference", "Visual Motion Sensitivity", "Screen Brightness Preference"],
            "accommodation": "Audio dampening, muted color palette, zero background movement"
        },
        "cognitive_flexibility_index": {
            "score": f"{flexibility_score}/3",
            "level": "Enhanced Transition Support Needed" if flexibility_score >= 2 else "Standard Transition",
            "items_analyzed": ["Task Transition Cadence", "Activity Switching Buffer", "Initiation Support Need"],
            "accommodation": "1-minute calming breathers, visual progress checklists, starter hint helper"
        },
        "reading_and_decoding_index": {
            "score": f"{reading_score}/3",
            "level": "Enhanced Reading Support" if reading_score >= 2 else "Standard Reading Support",
            "items_analyzed": ["Visual Text Spacing", "Letter Spacing Preference", "Text-to-Speech Readiness"],
            "accommodation": "OpenDyslexic font typography, high text tracking, on-demand read-aloud"
        },
        "attention_and_pacing_index": {
            "score": f"{attention_score}/3",
            "level": "Untimed Focus Priority" if attention_score >= 2 else "Standard Pacing",
            "items_analyzed": ["Visual Element Focus", "Sustained Focus Preference", "Timer Pressure Tolerance"],
            "accommodation": "Untimed exploratory pacing, focused task card spotlight, 1-2 min micro-units"
        },
        "medical_developmental_profile": {
            "neurodevelopmental_history_flag": False,
            "items_analyzed": ["Environmental Learning Support", "Adaptive Scaffold Cadence"],
            "status": "Strictly Educational Support Baseline"
        }
    }

    # Recommended Accommodations Summary
    accommodations = [
        "High contrast, OpenDyslexic font typography option for visual decoding",
        "Spacious layout density with zero flashing/moving background elements",
        "Always-accessible text-to-speech audio reader button",
        "Untimed exploratory pacing without countdown clock anxiety",
        "Step-by-step hint ladder with positive, non-punitive retry feedback",
        "Sensory rest timers and 1-minute calming breathers between quest milestones"
    ]

    # Initial UI Configuration
    initial_ui = {
        "visual_density": "spacious" if density_low else "balanced",
        "guidance_level": "high" if step_pref else "moderate",
        "task_size": "small" if task_small else "medium",
        "audio_mode": "on_demand" if audio_high else "standard",
        "animation_level": "none" if attention_high else "gentle",
        "calm_mode": True if timer_sensitive or is_high(q16) else False,
        "palette": "soft" if is_high(q16) else "balanced",
        "font_family": "OpenDyslexic" if is_high(q17) else "Inter",
        "breather_type": "breathing" if timer_sensitive else "rhythm" if attention_high else "calm_space"
    }

    # Structured dimensions list for rendering
    dimensions_list = [
        BaselineSupportDimension(
            dimension_key="ATTENTION_SUPPORT",
            title="Attention & Focus Support",
            support_level=attention_support,
            recommended_strategy="Minimize background animations; highlight active card with gentle contrast.",
            rationale="Derived from ADHD Item 2 (sustained attention) and ADHD Item 8 (visual distractibility)."
        ),
        BaselineSupportDimension(
            dimension_key="INSTRUCTION_STYLE",
            title="Instruction Style & Guidance",
            support_level=instruction_style,
            recommended_strategy="Break multi-step prompts into single-clause, sequential cards.",
            rationale="Derived from AQ-10 Item A2 (detail focus) and AQ-10 Item A6 (literal language)."
        ),
        BaselineSupportDimension(
            dimension_key="INFORMATION_DENSITY_SUPPORT",
            title="Information Density & Layout",
            support_level=information_density,
            recommended_strategy="Ample whitespace, large touch targets, single-concept focus per viewport.",
            rationale="Derived from Sensory Item 20 (glare sensitivity) and Dyslexia Item 6 (letter crowding)."
        ),
        BaselineSupportDimension(
            dimension_key="CONTENT_REPRESENTATION",
            title="Content Modality & Representation",
            support_level=content_rep,
            recommended_strategy="Pair diagrams and visual metaphors with optional audio narration.",
            rationale="Derived from AQ-10 Item A8 (concrete logic) and Dyslexia Item 4 (text-to-speech reader)."
        ),
        BaselineSupportDimension(
            dimension_key="TASK_GRANULARITY",
            title="Task Chunking & Granularity",
            support_level=task_granularity,
            recommended_strategy="Decompose curriculum objectives into 1-to-2 minute micro-quests.",
            rationale="Derived from AQ-10 Item A4 (task switching) and ADHD Item 6 (initiation friction)."
        ),
        BaselineSupportDimension(
            dimension_key="PACE_SUPPORT",
            title="Pacing & Time Pressure",
            support_level=pace_support,
            recommended_strategy="Remove visible clocks; allow learner full autonomy over completion pace.",
            rationale="Derived from WALS Dataset timer anxiety benchmark (mitigating countdown pressure)."
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
            rationale="Derived from WALS resilience metrics: preserves dopamine and confidence."
        ),
        BaselineSupportDimension(
            dimension_key="REPETITION_SUPPORT",
            title="Reinforcement & Spiral Review",
            support_level=repetition_support,
            recommended_strategy="Revisit core concepts using personalized interests (Space, Animals, Robotics).",
            rationale="Derived from AQ-10 Item A7: avoids abstract social ambiguity through high-interest anchors."
        ),
        BaselineSupportDimension(
            dimension_key="TRANSITION_SUPPORT",
            title="Transitions & Sensory Balance",
            support_level=transition_support,
            recommended_strategy="Provide clear completion cues and optional 1-minute breathing checkpoints.",
            rationale="Derived from AQ-10 Item A4 (task switching friction) and Item A10 (peer environment balance)."
        )
    ]

    return BaselineSupportProfile(
        student_id=student_id,
        student_name=student_name,
        caretaker_id=caretaker_id,
        version="baseline-v2-dataset-aligned",
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
        clinical_domain_indices=clinical_domain_indices,
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

    # 4. Save persistent student snapshot to disk
    await save_persistent_students(db)

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
    user_email = current_user.get("email")
    
    # Query learners where caretaker_id matches user id or user email
    query = {"$or": [
        {"caretaker_id": caretaker_id},
        {"caregiver_id": caretaker_id},
        {"caretaker_email": user_email}
    ]}
    
    cursor = db["learners"].find(query).sort("created_at", -1)
    learners = await cursor.to_list(length=50)

    # If no learners found in memory, load persistent store and re-check
    if not learners:
        await load_persistent_students(db)
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
            age=int(l.get("age") or 11),
            grade=l.get("grade", "Class 6"),
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
    Fetches a specific student with resilient ownership recovery.
    """
    db = get_database()
    caretaker_id = str(current_user.get("id"))
    student = await find_or_recover_student(db, student_id, current_user)
    
    if not student:
        raise HTTPException(status_code=404, detail="Student record not found.")

    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    is_valid_owner = (
        not student_caretaker
        or student_caretaker == caretaker_id
        or student.get("caretaker_email") == current_user.get("email")
        or current_user.get("role") in ["CAREGIVER", "caregiver", "ADMIN", "admin", "EDUCATOR"]
    )
    if not is_valid_owner:
        raise HTTPException(status_code=403, detail="Unauthorized access: You do not have permission to view this student.")

    first_name = student.get("first_name") or student.get("name", "Student").split(" ")[0]
    return StudentResponse(
        id=str(student.get("_id", student_id)),
        caretaker_id=student_caretaker or caretaker_id,
        first_name=first_name,
        name=student.get("name", first_name),
        age=int(student.get("age") or 11),
        grade=student.get("grade", "Class 6"),
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

    # Resilient student recovery
    student = await find_or_recover_student(db, student_id, current_user)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    is_valid_owner = (
        not student_caretaker
        or student_caretaker == caretaker_id
        or student.get("caretaker_email") == current_user.get("email")
        or current_user.get("role") in ["CAREGIVER", "caregiver", "ADMIN", "admin", "EDUCATOR"]
    )
    if not is_valid_owner:
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    # Retrieve draft if exists
    resolved_student_id = str(student.get("_id", student_id))
    draft_doc = await db["questionnaire_drafts"].find_one({
        "$or": [{"student_id": student_id}, {"student_id": resolved_student_id}]
    })
    draft_data = {
        "responses": draft_doc.get("responses", {}) if draft_doc else {},
        "current_question": draft_doc.get("current_question", 1) if draft_doc else 1
    }

    return {
        "schema": QUESTIONNAIRE_20_SCHEMA,
        "student": {
            "id": resolved_student_id,
            "name": student.get("name", "Student"),
            "first_name": student.get("first_name", student.get("name", "Student")),
            "age": student.get("age", 11),
            "grade": student.get("grade", "Class 6")
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

    # Resilient student recovery
    student = await find_or_recover_student(db, student_id, current_user)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    is_valid_owner = (
        not student_caretaker
        or student_caretaker == caretaker_id
        or student.get("caretaker_email") == current_user.get("email")
        or current_user.get("role") in ["CAREGIVER", "caregiver", "ADMIN", "admin", "EDUCATOR"]
    )
    if not is_valid_owner:
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    resolved_id = str(student.get("_id", student_id))
    await db["questionnaire_drafts"].update_one(
        {"student_id": resolved_id},
        {
            "$set": {
                "student_id": resolved_id,
                "caretaker_id": caretaker_id,
                "responses": draft.responses,
                "current_question": draft.current_question,
                "updated_at": datetime.utcnow()
            }
        },
        upsert=True
    )
    await save_persistent_students(db)
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

    # Resilient student recovery
    student = await find_or_recover_student(db, student_id, current_user)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    is_valid_owner = (
        not student_caretaker
        or student_caretaker == caretaker_id
        or student.get("caretaker_email") == current_user.get("email")
        or current_user.get("role") in ["CAREGIVER", "caregiver", "ADMIN", "admin", "EDUCATOR"]
    )
    if not is_valid_owner:
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    resolved_id = str(student.get("_id", student_id))
    student_name = student.get("name", "Student")
    responses = submission.responses

    # 1. Compute 10 Educational Support Dimensions (Strictly non-diagnostic)
    profile = compute_baseline_support_dimensions(
        student_id=resolved_id,
        student_name=student_name,
        caretaker_id=caretaker_id,
        responses=responses
    )

    # 2. Persist baseline support profile in MongoDB
    profile_dict = profile.model_dump()
    await db["baseline_support_profiles"].update_one(
        {"student_id": resolved_id},
        {"$set": profile_dict},
        upsert=True
    )

    # 3. Mark student as completed screening
    query = {"_id": ObjectId(resolved_id)} if ObjectId.is_valid(resolved_id) else {"id": resolved_id}
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
        "learner_id": resolved_id,
        "caregiver_id": caretaker_id,
        "learner_name": student_name,
        "learner_age": student.get("age", 11),
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
        {"learner_id": resolved_id},
        {"$set": runtime_profile},
        upsert=True
    )

    # Also set active learner for caretaker user
    await db["users"].update_many(
        {"$or": [{"_id": ObjectId(current_user["id"])} if ObjectId.is_valid(current_user["id"]) else {"id": current_user["id"]},
                 {"email": current_user.get("email")}]},
        {"$set": {"learner_id": resolved_id, "learner_name": student_name}}
    )

    # 5. Clean up draft & save persistent store
    await db["questionnaire_drafts"].delete_one({"student_id": resolved_id})
    await save_persistent_students(db)

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

    # Resilient student recovery
    student = await find_or_recover_student(db, student_id, current_user)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
        
    student_caretaker = str(student.get("caretaker_id", student.get("caregiver_id", "")))
    is_valid_owner = (
        not student_caretaker
        or student_caretaker == caretaker_id
        or student.get("caretaker_email") == current_user.get("email")
        or current_user.get("role") in ["CAREGIVER", "caregiver", "ADMIN", "admin", "EDUCATOR"]
    )
    if not is_valid_owner:
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    resolved_id = str(student.get("_id", student_id))
    profile_doc = await db["baseline_support_profiles"].find_one({
        "$or": [{"student_id": student_id}, {"student_id": resolved_id}]
    })
    if not profile_doc:
        # If screening was not completed, compute default baseline so caregiver can preview
        profile = compute_baseline_support_dimensions(
            student_id=resolved_id,
            student_name=student.get("name", "Student"),
            caretaker_id=caretaker_id,
            responses={}
        )
        profile_doc = profile.model_dump()

    return BaselineSupportProfile(**profile_doc)

