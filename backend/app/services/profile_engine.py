import logging
from typing import Dict, Any, List, Tuple
from app.models.questionnaire import (
    CaregiverQuestionnaireInput,
    InitialLearnerSupportProfile,
    CaregiverQuestionnaireComprehensiveInput
)
from app.models.learner_profile import (
    LearnerProfile, VisualPreferences, SensoryPreferences,
    MotivationPreferences, InteractionPreferences
)

logger = logging.getLogger("neuroquest.profile_engine")

COLOR_HEX_MAP = {
    "blue": "#3b82f6",
    "purple": "#8b5cf6",
    "teal": "#14b8a6",
    "green": "#10b981",
    "pink": "#ec4899",
    "indigo": "#6366f1",
    "amber": "#f59e0b",
    "orange": "#f97316",
    "sky": "#0284c7",
    "violet": "#7c3aed",
    "yellow": "#eab308",
    "emerald": "#059669"
}

COMPLEMENTARY_COLOR_MAP = {
    "#3b82f6": "#8b5cf6",
    "#8b5cf6": "#ec4899",
    "#14b8a6": "#059669",
    "#10b981": "#3b82f6",
    "#ec4899": "#8b5cf6",
    "#6366f1": "#14b8a6",
    "#f59e0b": "#f97316",
    "#f97316": "#f59e0b",
    "#0284c7": "#3b82f6",
    "#7c3aed": "#ec4899"
}

def determine_primary_color(favorite: str, avoided: List[str]) -> str:
    fav_clean = favorite.strip().lower()
    avoided_clean = [c.strip().lower() for c in avoided]
    
    # Check if favorite matches known color hex
    selected_hex = "#3b82f6" # default blue
    for name, hex_val in COLOR_HEX_MAP.items():
        if name in fav_clean and name not in avoided_clean:
            selected_hex = hex_val
            break
            
    # Avoid red/harsh colors if specified
    if "red" in avoided_clean or "bright red" in avoided_clean:
        if selected_hex in ["#f97316", "#ec4899"]: # replace warm reds with soft teal or blue
            selected_hex = "#14b8a6"
            
    return selected_hex

def determine_background_theme(themes: List[str], enjoyed_topics: str) -> str:
    combined = " ".join(themes).lower() + " " + enjoyed_topics.lower()
    
    if "space" in combined or "planet" in combined or "star" in combined or "galaxy" in combined:
        return "space"
    elif "animal" in combined or "pet" in combined or "dog" in combined or "cat" in combined or "wild" in combined:
        return "animals"
    elif "coding" in combined or "technology" in combined or "robot" in combined or "computer" in combined:
        return "coding"
    elif "nature" in combined or "plant" in combined or "outdoor" in combined or "forest" in combined:
        return "nature"
    elif "fantasy" in combined or "magic" in combined or "dragon" in combined:
        return "fantasy"
    elif "art" in combined or "draw" in combined or "paint" in combined:
        return "art"
    elif "music" in combined or "song" in combined or "instrument" in combined:
        return "music"
    elif "sport" in combined or "game" in combined or "ball" in combined:
        return "sports"
    return "space" # default theme motif

def process_questionnaire_to_profile(
    questionnaire: CaregiverQuestionnaireInput,
    learner_id: str,
    caregiver_id: str,
    learner_name: str = "Learner"
) -> LearnerProfile:
    
    # 1. Colors & Theme
    primary_color = determine_primary_color(
        questionnaire.q6_favorite_color,
        questionnaire.q7_disliked_colors
    )
    secondary_color = COMPLEMENTARY_COLOR_MAP.get(primary_color, "#8b5cf6")
    background_theme = determine_background_theme(
        questionnaire.q3_themes,
        questionnaire.q1_enjoyed_topics
    )
    
    # Palette type normalization
    palette_raw = questionnaire.q8_color_palette_preference.lower()
    if "dark" in palette_raw:
        palette_type = "dark"
    elif "contrast" in palette_raw:
        palette_type = "high_contrast"
    elif "bright" in palette_raw:
        palette_type = "bright"
    elif "minimal" in palette_raw:
        palette_type = "minimal"
    else:
        palette_type = "soft"
        
    # Font style
    # Check accommodations from 20-question assessment
    accommodations = getattr(questionnaire, "q20_accommodations", []) or []
    has_dyslexic_font = any("dyslexic" in str(a).lower() for a in accommodations)
    has_reduced_motion = any("reduced motion" in str(a).lower() or "motion" in str(a).lower() for a in accommodations)
    
    font_family = "OpenDyslexic" if has_dyslexic_font else ("rounded" if palette_type == "soft" else "sans")
    
    # 9. Content density & text tolerance
    density_pref = getattr(questionnaire, "q9_content_density", "") or ""
    if "single-concept" in density_pref.lower() or "minimal" in density_pref.lower():
        visual_density = "minimal"
    elif "dual-card" in density_pref.lower() or questionnaire.q12_prefer_calm_screen:
        visual_density = "spacious"
    else:
        visual_density = "balanced"

    visual_prefs = VisualPreferences(
        favorite_colors=[questionnaire.q6_favorite_color],
        avoided_colors=questionnaire.q7_disliked_colors,
        palette_type=palette_type,
        visual_style=questionnaire.q9_visual_style_preference,
        primary_color=primary_color,
        secondary_color=secondary_color,
        background_theme=background_theme,
        font_family=font_family,
        font_scale="medium"
    )
    
    # 2. Sensory Preferences
    anim_raw = (getattr(questionnaire, "q8_distraction_sensitivity", "") or questionnaire.q10_animation_effect).lower()
    if has_reduced_motion or "high" in anim_raw or "distract" in anim_raw:
        anim_intensity = "none"
    elif "moderate" in anim_raw:
        anim_intensity = "low"
    else:
        anim_intensity = "normal"
        
    audio_pref = getattr(questionnaire, "q5_audio_support", "").lower()
    sound_enabled = "automatic" in audio_pref or "on-demand" in audio_pref or "help" in questionnaire.q11_sound_effect.lower()
    
    sensory_prefs = SensoryPreferences(
        sound_enabled=sound_enabled,
        sound_preference="calm_chimes" if sound_enabled else "quiet",
        animation_intensity=anim_intensity,
        visual_density=visual_density,
        calm_mode=questionnaire.q12_prefer_calm_screen or "high" in anim_raw
    )
    
    # 3. Motivation
    reinforce_pref = getattr(questionnaire, "q18_reinforcement_style", "")
    reward_types = questionnaire.q21_reward_types.copy()
    if reinforce_pref:
        reward_types.append(reinforce_pref)
        
    motivation_prefs = MotivationPreferences(
        preferred_rewards=reward_types,
        reward_style="badges_unlocks" if any("unlock" in str(r).lower() for r in reward_types) else "collectables"
    )
    
    # 4. Interaction Preferences
    chunking_pref = getattr(questionnaire, "q10_task_chunking", "").lower()
    guidance_pref = getattr(questionnaire, "q16_step_guidance", "").lower()
    break_pref = getattr(questionnaire, "q17_break_frequency", "").lower()
    
    task_size = "small" if ("micro" in chunking_pref or "short" in chunking_pref or "small" in questionnaire.q16_task_structure.lower()) else "medium"
    guidance = "high" if ("always" in guidance_pref or "high" in guidance_pref or "step" in questionnaire.q16_task_structure.lower()) else "moderate"
    break_frequency = 6 if ("5 to 7" in break_pref or "every 3" in break_pref) else 10
    
    interaction_prefs = InteractionPreferences(
        task_size=task_size,
        feedback_style=questionnaire.q19_feedback_style,
        guidance_level=guidance,
        break_frequency_mins=break_frequency
    )
    
    # 5. Extract interests list
    interests = (questionnaire.q3_themes or ["Space", "Animals"]).copy()
    if questionnaire.q1_enjoyed_topics:
        interests.append(questionnaire.q1_enjoyed_topics)
    if questionnaire.q5_voluntary_subjects:
        interests.append(questionnaire.q5_voluntary_subjects)
        
    hobbies = [h.strip() for h in questionnaire.q4_hobbies.split(",") if h.strip()] if questionnaire.q4_hobbies else []
    
    return LearnerProfile(
        learner_id=learner_id,
        caregiver_id=caregiver_id,
        learner_name=learner_name,
        interests=interests,
        hobbies=hobbies,
        preferred_learning_modes=questionnaire.q15_learning_modality,
        visual_preferences=visual_prefs,
        sensory_preferences=sensory_prefs,
        motivation=motivation_prefs,
        interaction_preferences=interaction_prefs,
        avoidance_keywords=[w.strip() for w in questionnaire.q24_platform_avoidances.split(",") if w.strip()] if questionnaire.q24_platform_avoidances else [],
        calming_strategies=[c.strip() for c in questionnaire.q23_calming_methods.split(",") if c.strip()] if questionnaire.q23_calming_methods else ["Gentle breathing", "Sensory pause"]
    )

def process_comprehensive_questionnaire_to_support_profile(
    input_data: Any,
    learner_id: str,
    caregiver_id: str,
    learner_name: str = "Learner"
) -> Tuple[InitialLearnerSupportProfile, LearnerProfile]:
    """
    Translates 10-step comprehensive questionnaire responses into both:
    1. The 14-dimension InitialLearnerSupportProfile (research/pedagogical model)
    2. The active LearnerProfile (operational runtime UI/theming model)
    """
    from datetime import datetime
    from app.models.questionnaire import InitialLearnerSupportProfile, CaregiverQuestionnaireComprehensiveInput

    # Normalize to dict or object
    data = input_data.model_dump() if hasattr(input_data, "model_dump") else (input_data.dict() if hasattr(input_data, "dict") else dict(input_data))

    name = data.get("learner_name") or learner_name or "Learner"
    grade = data.get("grade_level") or "Class 6"
    subjects = data.get("primary_subjects") or ["Science", "Mathematics"]
    interests = data.get("interest_anchors") or ["Space", "Animals"]
    theme_anchor = determine_background_theme(interests, " ".join(interests))

    has_support = data.get("has_identified_support") or "No"
    support_cats = data.get("support_categories") or [] if has_support == "Yes" else []

    rep_modes = data.get("representation_mode") or ["Visual diagrams, charts & infographics"]
    eng_anchors = data.get("engagement_anchors") or ["Exploration quests", "Visual puzzles"]
    
    reading_vol = data.get("reading_text_volume") or "Bite-sized sentences (1 to 2 lines per card)"
    academic_trig = data.get("academic_triggers") or ["Dense reading passages"]
    diff_resp = data.get("difficulty_response") or "Smaller steps"

    task_mgmt = data.get("task_management_friction") or ["Starting a task", "Organizing work"]
    frust_behavior = data.get("frustration_behavior") or "Offer a 1-minute calming sensory break"
    session_pattern = data.get("session_fatigue_pattern") or "Prefers short micro-sessions"

    vis_access = data.get("visual_accessibility") or ["Clear visual headings", "Reduced motion/animation"]
    audio_pref = data.get("audio_preferences") or "On-demand audio button (listen when helpful)"
    palette_choice = data.get("color_palette") or "Soft calming pastels"

    instr_granularity = data.get("instruction_granularity") or "Single-clause direct instructions"
    feedback_style = data.get("feedback_style") or "Show the first step"
    pacing = data.get("pacing_control") or "Completely untimed, relaxed exploration"

    accommodations = data.get("accommodations_used") or ["Additional time", "Visual instructions"]
    goals = data.get("learner_goals") or ["Confidence in Science", "Independent study skills"]

    # 1. Construct 14-Dimension Initial Learning Support Profile
    sensory_dict = {
        "sound_enabled": "quiet" not in audio_pref.lower() and "mute" not in audio_pref.lower(),
        "audio_mode": "automatic" if "automatic" in audio_pref.lower() else "on_demand",
        "visual_density": "spacious" if "bite-sized" in reading_vol.lower() or "fewer" in str(vis_access).lower() else "balanced",
        "palette": "soft" if "soft" in palette_choice.lower() else ("high_contrast" if "contrast" in palette_choice.lower() else "minimal"),
        "animation_level": "none" if any("reduced motion" in a.lower() for a in vis_access) else "gentle"
    }

    support_profile = InitialLearnerSupportProfile(
        learner_id=learner_id,
        caregiver_id=caregiver_id,
        learner_name=name,
        grade_level=grade,
        primary_subjects=subjects,
        theme_anchor=theme_anchor,
        learning_representation=rep_modes if isinstance(rep_modes, list) else [rep_modes],
        instruction_style=[instr_granularity],
        task_size_preference="small" if "bite-sized" in reading_vol.lower() or "micro" in session_pattern.lower() else "medium",
        session_length_preference=session_pattern,
        feedback_style=[feedback_style, "Encouraging positive reinforcement"],
        scaffolding_preference=[diff_resp, "Step-by-step ladder"],
        engagement_preferences=eng_anchors if isinstance(eng_anchors, list) else [eng_anchors],
        observed_learning_difficulties=academic_trig if isinstance(academic_trig, list) else [academic_trig],
        task_management_support=task_mgmt if isinstance(task_mgmt, list) else [task_mgmt],
        accessibility_preferences=vis_access if isinstance(vis_access, list) else [vis_access],
        sensory_preferences=sensory_dict,
        existing_accommodations=accommodations if isinstance(accommodations, list) else [accommodations],
        caregiver_reported_support_information=support_cats if isinstance(support_cats, list) else [support_cats],
        learner_goals=goals if isinstance(goals, list) else [goals],
        consent={"granted": True, "timestamp": str(datetime.utcnow())},
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    # 2. Derive Operational LearnerProfile
    has_dyslexic = any("dyslexic" in str(a).lower() for a in vis_access) or any("dyslexic" in str(a).lower() for a in accommodations)
    font_family = "OpenDyslexic" if has_dyslexic else ("rounded" if sensory_dict["palette"] == "soft" else "sans")
    
    primary_color = "#3b82f6"
    if "green" in str(palette_choice).lower():
        primary_color = "#10b981"
    elif "teal" in str(palette_choice).lower():
        primary_color = "#14b8a6"
    elif "purple" in str(palette_choice).lower():
        primary_color = "#8b5cf6"

    visual_prefs = VisualPreferences(
        favorite_colors=[primary_color],
        avoided_colors=[],
        palette_type=sensory_dict["palette"],
        visual_style="visual_cards",
        primary_color=primary_color,
        secondary_color=COMPLEMENTARY_COLOR_MAP.get(primary_color, "#8b5cf6"),
        background_theme=theme_anchor,
        font_family=font_family,
        font_scale="large" if any("larger text" in str(a).lower() for a in vis_access) else "medium"
    )

    sensory_prefs = SensoryPreferences(
        sound_enabled=sensory_dict["sound_enabled"],
        sound_preference="gentle_chimes" if sensory_dict["sound_enabled"] else "quiet",
        animation_intensity=sensory_dict["animation_level"],
        visual_density=sensory_dict["visual_density"],
        calm_mode=True
    )

    motivation_prefs = MotivationPreferences(
        preferred_rewards=[data.get("celebration_style") or "Area unlocks & stars"],
        reward_style="badges_unlocks"
    )

    interaction_prefs = InteractionPreferences(
        task_size=support_profile.task_size_preference,
        feedback_style="immediate_supportive",
        guidance_level="high",
        break_frequency_mins=6 if "5 to 7" in data.get("break_rhythm", "") else 10
    )

    operational_profile = LearnerProfile(
        learner_id=learner_id,
        caregiver_id=caregiver_id,
        learner_name=name,
        interests=interests,
        hobbies=[],
        preferred_learning_modes=rep_modes,
        visual_preferences=visual_prefs,
        sensory_preferences=sensory_prefs,
        motivation=motivation_prefs,
        interaction_preferences=interaction_prefs,
        avoidance_keywords=["timed tests", "flash animations"],
        calming_strategies=[frust_behavior, "1-minute sensory pause"]
    )

    return support_profile, operational_profile

def generate_safe_pedagogical_instructions(profile: InitialLearnerSupportProfile) -> str:
    """
    Translates the learner support profile into safe pedagogical LLM system instructions.
    Strictly Non-Diagnostic: Contains ZERO clinical labels, DSM-5 or ICD codes.
    """
    instructions = [
        f"You are an encouraging, patient educational AI mentor for {profile.learner_name}.",
        f"Theme Anchor: Connect concept analogies to {profile.theme_anchor.upper()} and {', '.join(profile.primary_subjects)}.",
        f"Instructional Format: Deliver explanations in {profile.instruction_style[0].lower()}.",
        f"Scaffolding Method: When the learner struggles, provide a gentle hint first or {profile.scaffolding_preference[0].lower()}.",
        "Pacing: Keep explanations bite-sized with zero timed pressure.",
        "Tone: Warm, validating, non-punitive, celebrating incremental effort and curiosity."
    ]
    return " ".join(instructions)

