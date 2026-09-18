from fastapi import APIRouter, HTTPException, status, Depends, Request
from datetime import datetime
from typing import Dict, Any, List, Optional
from app.models.questionnaire import (
    CaregiverQuestionnaireInput,
    CaregiverQuestionnaireResponse,
    CaregiverQuestionnaireComprehensiveInput,
    InitialLearnerSupportProfile,
    QuestionnaireDraft
)
from app.models.learner_profile import LearnerProfile
from app.database import get_database
from app.services.auth_service import get_current_user
from app.services.profile_engine import (
    process_questionnaire_to_profile,
    process_comprehensive_questionnaire_to_support_profile,
    generate_safe_pedagogical_instructions
)

router = APIRouter(prefix="/api/onboarding", tags=["Onboarding"])

# ----------------------------------------------------
# 10-STEP QUESTIONNAIRE SCHEMA DEFINITION (28 Questions)
# ----------------------------------------------------
QUESTIONNAIRE_SCHEMA = {
    "title": "NeuroQuest Caregiver Onboarding Questionnaire",
    "version": "2.0",
    "description": "Constructs the learner's Initial Learning Support Profile from research-informed educational variables.",
    "total_steps": 10,
    "total_questions": 28,
    "disclaimer": "NeuroQuest is an educational support platform. This questionnaire is non-diagnostic and strictly configures educational, sensory, and accessibility accommodations. Zero medical diagnoses are computed or assigned.",
    "steps": [
        {
            "step": 1,
            "title": "Learner & Education",
            "category": "Category A — Pedagogical Content",
            "description": "Basic educational context and special interest passion domains.",
            "questions": [
                {
                    "id": "learner_name",
                    "title": "What is the learner's preferred name?",
                    "type": "text",
                    "default": "Learner",
                    "required": True
                },
                {
                    "id": "grade_level",
                    "title": "What is the learner's current grade band?",
                    "type": "single_choice",
                    "options": ["Class 6 (NCERT)", "Class 7 (NCERT)", "Class 8 (NCERT)", "Other / Flexible"],
                    "default": "Class 6 (NCERT)",
                    "required": True
                },
                {
                    "id": "primary_subjects",
                    "title": "Which subjects are the primary focus for learning support?",
                    "type": "multi_choice",
                    "options": ["Science", "Mathematics", "Social Science", "Logic & Puzzles", "English & Vocabulary"],
                    "default": ["Science", "Mathematics"],
                    "required": True
                },
                {
                    "id": "interest_anchors",
                    "title": "What are the learner's high-interest passion topics?",
                    "type": "multi_choice",
                    "options": ["Space & Astronomy", "Animals & Nature", "Coding & Robotics", "Fantasy & Mythology", "Art & Drawing", "Vehicles & Transport", "Music & Rhythm"],
                    "default": ["Space & Astronomy", "Animals & Nature"],
                    "required": True
                }
            ]
        },
        {
            "step": 2,
            "title": "Known Support Information (Optional)",
            "category": "Category C — Educational Accommodations",
            "description": "Optional section. Information provided here is used solely to activate existing school/educational supports.",
            "is_optional": True,
            "questions": [
                {
                    "id": "has_identified_support",
                    "title": "Has the learner been identified by a school or specialist as having an educational learning or support need?",
                    "type": "single_choice",
                    "options": ["Yes", "No", "Unsure", "Prefer not to say"],
                    "default": "No",
                    "required": False
                },
                {
                    "id": "support_categories",
                    "title": "Which general areas of educational support are relevant?",
                    "type": "multi_choice",
                    "options": ["Attention & Focus Support", "Reading & Dyslexia Support", "Writing & Fine Motor Support", "Mathematics & Processing Support", "Social & Communication Support", "Sensory Regulation Support", "Other Educational Need"],
                    "depends_on": {"field": "has_identified_support", "value": "Yes"},
                    "default": [],
                    "required": False
                }
            ]
        },
        {
            "step": 3,
            "title": "Learning Strengths & Representation",
            "category": "Category A — Pedagogical Representation",
            "description": "How the learner best takes in, processes, and explores new ideas.",
            "questions": [
                {
                    "id": "representation_mode",
                    "title": "What type of material usually helps the learner understand a new topic best?",
                    "type": "multi_choice",
                    "options": ["Visual diagrams, charts & infographics", "Step-by-step worked examples", "Short bite-sized text", "Interactive animations & simulations", "Audio narration & speech", "Hands-on puzzle exploration"],
                    "default": ["Visual diagrams, charts & infographics", "Step-by-step worked examples"],
                    "required": True
                },
                {
                    "id": "engagement_anchors",
                    "title": "Which learning activities consistently keep the learner engaged?",
                    "type": "multi_choice",
                    "options": ["Exploration quests & territory unlocks", "Visual logic puzzles", "Step-by-step mystery solving", "Card collecting & badges", "Story-driven missions with characters"],
                    "default": ["Exploration quests & territory unlocks", "Visual logic puzzles"],
                    "required": True
                },
                {
                    "id": "interest_boost",
                    "title": "How much does connecting lessons to their special interest improve focus?",
                    "type": "single_choice",
                    "options": ["Greatly helps (doubles engagement)", "Moderately helps", "Neutral / Depends on topic"],
                    "default": "Greatly helps (doubles engagement)",
                    "required": True
                }
            ]
        },
        {
            "step": 4,
            "title": "Learning Difficulties & Processing",
            "category": "Category A & B — Cognitive Load Management",
            "description": "Identifying friction points to apply proactive UI chunking.",
            "questions": [
                {
                    "id": "reading_text_volume",
                    "title": "What amount of continuous reading text is most comfortable per screen?",
                    "type": "single_choice",
                    "options": ["Bite-sized sentences (1 to 2 lines per card)", "Short paragraphs (3 to 4 lines)", "Bullet points with icons", "Standard story passages"],
                    "default": "Bite-sized sentences (1 to 2 lines per card)",
                    "required": True
                },
                {
                    "id": "academic_triggers",
                    "title": "Which academic tasks usually trigger struggle or avoidance?",
                    "type": "multi_choice",
                    "options": ["Dense continuous reading passages", "Multi-step word problems", "Abstract definitions without examples", "Rapid mental calculation", "Open-ended ambiguous questions", "None noticed"],
                    "default": ["Dense continuous reading passages"],
                    "required": True
                },
                {
                    "id": "difficulty_response",
                    "title": "When a new topic is difficult, what usually helps most?",
                    "type": "single_choice",
                    "options": ["Break into smaller steps", "Show an easier parallel worked example first", "Visual diagram / infographic", "More conceptual explanation", "Additional guided practice"],
                    "default": "Break into smaller steps",
                    "required": True
                }
            ]
        },
        {
            "step": 5,
            "title": "Attention & Task Management",
            "category": "Category B — Executive Function Indicators",
            "description": "Executive function indicators translated into supportive scaffold tools.",
            "questions": [
                {
                    "id": "task_management_friction",
                    "title": "Which parts of independent learning are usually difficult?",
                    "type": "multi_choice",
                    "options": ["Starting a task (initiation friction)", "Staying focused on single screen", "Remembering multi-step instructions", "Switching between tasks / topics", "Completing tasks without checking out", "None noticed"],
                    "default": ["Starting a task (initiation friction)", "Staying focused on single screen"],
                    "required": True
                },
                {
                    "id": "frustration_behavior",
                    "title": "What usually happens when a task becomes frustrating or difficult?",
                    "type": "single_choice",
                    "options": ["Offer a 1-minute calming sensory break", "Requests a gentle hint immediately", "Wants to see the solution step-by-step", "Leaves task temporarily to reset", "Changes to an easier subject"],
                    "default": "Offer a 1-minute calming sensory break",
                    "required": True
                },
                {
                    "id": "session_fatigue_pattern",
                    "title": "How does the learner usually respond to longer learning sessions?",
                    "type": "single_choice",
                    "options": ["Prefers short micro-sessions (5 to 8 mins)", "Needs scheduled breaks every 10 to 12 mins", "Remains engaged for 15+ minutes if interested", "Depends heavily on subject"],
                    "default": "Prefers short micro-sessions (5 to 8 mins)",
                    "required": True
                }
            ]
        },
        {
            "step": 6,
            "title": "Accessibility & Sensory Preferences",
            "category": "Category B & C — Sensory Regulation",
            "description": "Configures color palette, contrast, typography, and motion intensity.",
            "questions": [
                {
                    "id": "visual_accessibility",
                    "title": "Which visual accessibility supports are helpful?",
                    "type": "multi_choice",
                    "options": ["Dyslexic-friendly font (OpenDyslexic)", "Larger text and generous line spacing", "Reduced motion (disable auto-sliding & animations)", "High contrast mode", "Fewer elements on screen (spacious layout)", "Clear visual breadcrumbs"],
                    "default": ["Dyslexic-friendly font (OpenDyslexic)", "Reduced motion (disable auto-sliding & animations)"],
                    "required": True
                },
                {
                    "id": "audio_preferences",
                    "title": "How should sound and audio read-aloud be configured?",
                    "type": "single_choice",
                    "options": ["On-demand audio button (listen when helpful)", "Automatic read-aloud narration on load", "Subtle pleasant chimes on success only", "Quiet mode (mute all sounds)"],
                    "default": "On-demand audio button (listen when helpful)",
                    "required": True
                },
                {
                    "id": "color_palette",
                    "title": "Which color palette style feels most comfortable?",
                    "type": "single_choice",
                    "options": ["Soft calming pastels (low sensory glare)", "High contrast dark mode", "Vibrant & playful colors", "Minimalist monochrome"],
                    "default": "Soft calming pastels (low sensory glare)",
                    "required": True
                }
            ]
        },
        {
            "step": 7,
            "title": "Communication & Instruction Preferences",
            "category": "Category A — Instructional Design",
            "description": "How the AI mentor interacts, gives feedback, and delivers hints.",
            "questions": [
                {
                    "id": "instruction_granularity",
                    "title": "How does the learner prefer instructions to be delivered?",
                    "type": "single_choice",
                    "options": ["Single-clause direct instructions (one action per card)", "Short bullet points with icons", "Concrete example shown first", "Visual diagram / flowchart"],
                    "default": "Single-clause direct instructions (one action per card)",
                    "required": True
                },
                {
                    "id": "feedback_style",
                    "title": "When the learner makes a mistake, what feedback style helps most?",
                    "type": "single_choice",
                    "options": ["Show the first step gently", "Provide a small clue without revealing answer", "Show a parallel worked example", "Explain gently why that option didn't work", "Let them retry with 2 options eliminated"],
                    "default": "Show the first step gently",
                    "required": True
                },
                {
                    "id": "pacing_control",
                    "title": "What pacing rhythm works best during learning tasks?",
                    "type": "single_choice",
                    "options": ["Completely untimed, relaxed exploration (zero clocks)", "Gentle recommended time suggestion", "Structured checkpoint countdowns"],
                    "default": "Completely untimed, relaxed exploration (zero clocks)",
                    "required": True
                }
            ]
        },
        {
            "step": 8,
            "title": "Existing Educational Accommodations",
            "category": "Category C — Established School Supports",
            "description": "Bridges school and IEP/504 accommodations into the digital interface.",
            "questions": [
                {
                    "id": "accommodations_used",
                    "title": "Does the learner currently use any educational supports in school or home?",
                    "type": "multi_choice",
                    "options": ["Additional time for tasks", "Shorter chunked assignments", "Scheduled visual breaks", "Visual step instructions", "Audio read-aloud / Text-to-speech", "Reduced visual clutter on paper/screen", "Alternative choices for demonstration", "None"],
                    "default": ["Additional time for tasks", "Visual step instructions", "Audio read-aloud / Text-to-speech"],
                    "required": True
                },
                {
                    "id": "effective_accommodations",
                    "title": "Which of these accommodations have proven most effective in practice?",
                    "type": "multi_choice",
                    "options": ["Additional time", "Visual instructions", "Audio reader", "Shorter tasks", "Scheduled breaks"],
                    "default": ["Visual instructions", "Additional time"],
                    "required": False
                }
            ]
        },
        {
            "step": 9,
            "title": "Learning Environment & Motivation",
            "category": "Category B — Motivation Architecture",
            "description": "Sensory surroundings and non-competitive celebration dynamics.",
            "questions": [
                {
                    "id": "study_environment",
                    "title": "Where and in what type of environment does the learner study best?",
                    "type": "single_choice",
                    "options": ["Quiet, distraction-minimized space", "Soft background instrumental music or white noise", "Active environment where physical fidgeting is okay"],
                    "default": "Quiet, distraction-minimized space",
                    "required": True
                },
                {
                    "id": "break_rhythm",
                    "title": "How often should the platform suggest a gentle sensory break?",
                    "type": "single_choice",
                    "options": ["Every 5 to 7 minutes with calm sensory animations", "Every 10 to 12 minutes", "Every 15 to 20 minutes", "Only when learner requests a pause"],
                    "default": "Every 5 to 7 minutes with calm sensory animations",
                    "required": True
                },
                {
                    "id": "celebration_style",
                    "title": "What type of achievement acknowledgment is preferred?",
                    "type": "single_choice",
                    "options": ["Visual unlocks (opening new planets, sanctuaries, or cyber parts)", "Quiet star count updates (minimal fanfare)", "Gentle celebratory animations", "Collection vault badges"],
                    "default": "Visual unlocks (opening new planets, sanctuaries, or cyber parts)",
                    "required": True
                }
            ]
        },
        {
            "step": 10,
            "title": "Consent, Review & Profile Generation",
            "category": "Privacy, Governance & Baseline Calibration",
            "description": "Review summary, verify educational consent, and generate the Initial Learning Support Profile.",
            "questions": [
                {
                    "id": "learner_goals",
                    "title": "What are the primary learning goals for this profile?",
                    "type": "multi_choice",
                    "options": ["Build confidence in STEM concepts", "Improve independent study persistence", "Enjoy stress-free learning exploration", "NCERT curriculum grade readiness", "Reduce homework frustration"],
                    "default": ["Build confidence in STEM concepts", "Improve independent study persistence"],
                    "required": True
                },
                {
                    "id": "consent_acknowledged",
                    "title": "Caregiver Educational Consent",
                    "type": "single_choice",
                    "options": ["I confirm this information is provided voluntarily to personalize educational delivery and understand NeuroQuest does not diagnose medical conditions."],
                    "default": "I confirm this information is provided voluntarily to personalize educational delivery and understand NeuroQuest does not diagnose medical conditions.",
                    "required": True
                }
            ]
        }
    ]
}

# ----------------------------------------------------
# ENDPOINTS
# ----------------------------------------------------

@router.get("/schema")
async def get_questionnaire_schema():
    """Returns the complete 10-step, 28-question schema for dynamic UI rendering."""
    return QUESTIONNAIRE_SCHEMA

@router.get("/draft")
async def get_questionnaire_draft(current_user: dict = Depends(get_current_user)):
    """Retrieves saved questionnaire draft for the authenticated caregiver."""
    db = get_database()
    caregiver_id = current_user["id"]
    draft = await db["questionnaire_drafts"].find_one({"caregiver_id": caregiver_id})
    if not draft:
        return {"step": 1, "form_data": {}, "exists": False}
    return {
        "step": draft.get("step", 1),
        "form_data": draft.get("form_data", {}),
        "updated_at": draft.get("updated_at"),
        "exists": True
    }

@router.post("/draft")
async def save_questionnaire_draft(
    draft_req: QuestionnaireDraft,
    current_user: dict = Depends(get_current_user)
):
    """Saves progress so caregivers can exit and resume anytime."""
    db = get_database()
    caregiver_id = current_user["id"]
    await db["questionnaire_drafts"].update_one(
        {"caregiver_id": caregiver_id},
        {
            "$set": {
                "step": draft_req.step,
                "form_data": draft_req.form_data,
                "updated_at": datetime.utcnow()
            }
        },
        upsert=True
    )
    return {"status": "saved", "step": draft_req.step, "saved_at": datetime.utcnow()}

@router.get("/profile")
async def get_initial_support_profile(current_user: dict = Depends(get_current_user)):
    """Retrieves the active 14-dimension InitialLearnerSupportProfile."""
    db = get_database()
    learner_id = current_user.get("learner_id")
    if not learner_id:
        raise HTTPException(status_code=404, detail="No learner linked to this user.")

    profile_doc = await db["initial_support_profiles"].find_one({"learner_id": learner_id})
    if not profile_doc:
        # Fallback to learner_preferences
        pref_doc = await db["learner_preferences"].find_one({"learner_id": learner_id})
        if not pref_doc:
            raise HTTPException(status_code=404, detail="Initial support profile not found.")
        return pref_doc

    profile_doc["id"] = str(profile_doc.get("_id", profile_doc.get("id", "")))
    if "_id" in profile_doc:
        del profile_doc["_id"]
    return profile_doc

@router.post("/questionnaire", response_model=LearnerProfile)
async def submit_questionnaire(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    """
    Submits the caregiver assessment questionnaire.
    Seamlessly handles both the comprehensive 10-step submission and legacy 20-field inputs.
    Generates both the 14-dimension InitialLearnerSupportProfile and active LearnerProfile.
    """
    db = get_database()
    caregiver_id = current_user["id"]
    learner_id = current_user.get("learner_id")

    # Parse JSON payload
    try:
        body = await request.json()
    except Exception:
        body = {}

    if not learner_id:
        caregiver_name = current_user.get("full_name") or current_user.get("username") or "Learner"
        learner_doc = {
            "caregiver_id": caregiver_id,
            "name": f"{caregiver_name}'s Learner",
            "created_at": datetime.utcnow()
        }
        l_res = await db["learners"].insert_one(learner_doc)
        learner_id = str(l_res.inserted_id)
        u_id = current_user.get("_id") or current_user.get("id")
        if u_id:
            await db["users"].update_one({"$or": [{"_id": u_id}, {"id": str(u_id)}]}, {"$set": {"learner_id": learner_id}})

    # Determine learner name
    learner_obj = await db["learners"].find_one({"_id": learner_id})
    learner_name = body.get("learner_name") or (learner_obj.get("name") if learner_obj else "Learner")

    # Check if payload is comprehensive 10-step or legacy 20-Q
    is_comprehensive = any(k in body for k in [
        "representation_mode", "academic_triggers", "task_management_friction",
        "visual_accessibility", "instruction_granularity", "learner_goals"
    ])

    if is_comprehensive:
        comp_input = CaregiverQuestionnaireComprehensiveInput(**body)
        support_profile, operational_profile = process_comprehensive_questionnaire_to_support_profile(
            input_data=comp_input,
            learner_id=learner_id,
            caregiver_id=caregiver_id,
            learner_name=learner_name
        )
        # Store support profile in initial_support_profiles
        supp_dict = support_profile.model_dump()
        supp_dict["caregiver_id"] = caregiver_id
        supp_dict["learner_id"] = learner_id
        await db["initial_support_profiles"].update_one(
            {"learner_id": learner_id},
            {"$set": supp_dict},
            upsert=True
        )
        profile = operational_profile
    else:
        # Legacy 20-Q path
        legacy_input = CaregiverQuestionnaireInput(**body)
        profile = process_questionnaire_to_profile(
            questionnaire=legacy_input,
            learner_id=learner_id,
            caregiver_id=caregiver_id,
            learner_name=learner_name
        )

    # Save responses to caregiver_profiles
    body_to_save = body.copy()
    body_to_save.update({
        "caregiver_id": caregiver_id,
        "learner_id": learner_id,
        "submitted_at": datetime.utcnow()
    })
    await db["caregiver_profiles"].insert_one(body_to_save)

    # Persist operational profile to learner_preferences
    profile_doc = profile.model_dump()
    profile_doc["updated_at"] = datetime.utcnow()
    await db["learner_preferences"].update_one(
        {"learner_id": learner_id},
        {"$set": profile_doc},
        upsert=True
    )

    # Seed initial progress and rewards if not exists
    existing_progress = await db["progress"].find_one({"learner_id": learner_id})
    if not existing_progress:
        badges = await db["rewards"].find().to_list(10)
        await db["progress"].insert_one({
            "learner_id": learner_id,
            "total_stars": 10,
            "total_tasks_completed": 0,
            "streak_days": 1,
            "subject_mastery": {
                "Mathematics": 0,
                "Science": 0,
                "English": 0,
                "General Knowledge": 0,
                "Coding/Logic": 0
            },
            "earned_badges": badges,
            "unlocked_themes": ["space", "animals", profile.visual_preferences.background_theme],
            "last_active": datetime.utcnow()
        })

    # Clear draft upon successful submission
    await db["questionnaire_drafts"].delete_one({"caregiver_id": caregiver_id})

    return profile
