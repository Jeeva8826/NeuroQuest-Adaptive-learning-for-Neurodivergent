import logging
from typing import Dict, Any

logger = logging.getLogger("neuroquest.adaptation_engine")

def compute_session_adaptations(
    learner_profile: Dict[str, Any],
    predicted_state_data: Dict[str, Any],
    task_performance: Dict[str, Any] = None,
    current_difficulty: int = 2
) -> Dict[str, Any]:
    
    state_name = predicted_state_data.get("state_name", "FOCUSED")
    confidence = predicted_state_data.get("confidence", 0.8)
    
    vis = learner_profile.get("visual_preferences", {})
    sens = learner_profile.get("sensory_preferences", {})
    inter = learner_profile.get("interaction_preferences", {})
    interests = learner_profile.get("interests", ["Space", "Exploration"])

    top_interest = interests[0] if interests else "Exploration"

    # Default adaptations
    difficulty_adj = "maintain"
    ui_mode = "normal"
    content_format = "normal"
    guidance_level = inter.get("guidance_level", "moderate")
    break_suggestion = False
    encouragement_msg = "You are doing great — keep going!"
    theme_adaptation = f"{top_interest} Quest"

    # Rule & ML-based State Adaptations
    if state_name == "FOCUSED":
        difficulty_adj = "maintain"
        ui_mode = "normal"
        content_format = "normal"
        guidance_level = "moderate"
        encouragement_msg = "Great focus! Ready for the next activity."

    elif state_name == "ATTENTION_DRIFT":
        difficulty_adj = "maintain"
        ui_mode = "focus" # Dim unrelated background, highlight current card
        content_format = "short_summary"
        guidance_level = "high"
        encouragement_msg = f"Let's focus on this quick {top_interest} challenge!"
        theme_adaptation = f"Special {top_interest} Mission"

    elif state_name == "POSSIBLE_FATIGUE":
        difficulty_adj = "decrease"
        ui_mode = "calm" # Muted colors, zero animations, spacious padding
        content_format = "step_by_step"
        guidance_level = "high"
        break_suggestion = True
        encouragement_msg = "You've worked hard! Want a 1-minute breather, or shall we make this easier?"

    elif state_name == "DISENGAGED":
        difficulty_adj = "decrease"
        ui_mode = "minimal"
        content_format = "visual_explanation"
        guidance_level = "high"
        break_suggestion = True
        encouragement_msg = f"Let's try a fun, bite-sized {top_interest} activity together!"
        theme_adaptation = f"Interactive {top_interest} Explorer"

    elif state_name == "HIGH_ENGAGEMENT":
        difficulty_adj = "increase"
        ui_mode = "normal"
        content_format = "normal"
        guidance_level = "low" # allow independent exploration
        encouragement_msg = "Awesome energy! Ready for a deeper challenge?"

    # Override if caregiver/learner prefers audio modality by default
    preferred_modes = learner_profile.get("preferred_learning_modes", [])
    if "Listening" in preferred_modes or sens.get("sound_enabled"):
        if ui_mode == "normal":
            ui_mode = "audio"

    return {
        "predicted_state": state_name,
        "confidence": confidence,
        "difficultyAdjustment": difficulty_adj,
        "uiMode": ui_mode,
        "contentFormat": content_format,
        "guidanceLevel": guidance_level,
        "breakSuggestion": break_suggestion,
        "encouragementMessage": encouragement_msg,
        "themeAdaptation": theme_adaptation,
        "primaryColor": vis.get("primary_color", "#3b82f6"),
        "secondaryColor": vis.get("secondary_color", "#8b5cf6"),
        "backgroundTheme": vis.get("background_theme", "space")
    }
