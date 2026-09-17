import logging
from typing import Dict, Any, List

logger = logging.getLogger("neuroquest.adaptation_explainer")

class AdaptationExplainerService:
    """Generates judge-friendly, non-medical summaries of platform adaptations."""

    def explain_adaptations(
        self,
        learner_profile: Dict[str, Any],
        predicted_state_data: Dict[str, Any] = None,
        adaptation_result: Dict[str, Any] = None
    ) -> Dict[str, Any]:

        state_name = predicted_state_data.get("state_name", "FOCUSED") if predicted_state_data else "FOCUSED"
        ui_mode = adaptation_result.get("uiMode", "normal") if adaptation_result else "normal"
        interests = learner_profile.get("interests", ["Space"])
        primary_interest = interests[0] if interests else "Space"

        reasons = []

        # 1. State / Engagement Adaptation Reasons
        if state_name == "FOCUSED":
            reasons.append("High focus detected: Maintaining steady challenge pace.")
        elif state_name == "ATTENTION_DRIFT":
            reasons.append("Attention drift pattern observed: Visual clutter dimmed & current task highlighted.")
        elif state_name == "POSSIBLE_FATIGUE":
            reasons.append("Fatigue signals detected: Reduced difficulty, muted screen contrast, and offered quiet breather.")
        elif state_name == "HIGH_ENGAGEMENT":
            reasons.append("Elevated engagement observed: Unlocking deeper exploration & independent guidance.")

        # 2. Interest Theme Reason
        reasons.append(f"Interest personalization: Wrapped learning objective in {primary_interest} narrative quest.")

        # 3. Gamification Motivation Reason
        motivation_types = learner_profile.get("gamification", {}).get("motivation_types", ["exploration"])
        primary_mot = motivation_types[0] if motivation_types else "exploration"
        reasons.append(f"Motivation alignment: Delivering non-competitive {primary_mot.capitalize()} rewards vs. past self.")

        # 4. Sensory / UI Mode Reason
        if ui_mode == "calm":
            reasons.append("Sensory adjustment: Activated Calm Mode with muted colors and zero flash animations.")
        elif ui_mode == "focus":
            reasons.append("Focus adjustment: Concentrated visual density around active task element.")

        return {
            "title": "Why NeuroQuest Adapted Today",
            "current_state": state_name,
            "ui_mode": ui_mode,
            "theme_applied": primary_interest,
            "adaptation_reasons": reasons,
            "non_medical_disclaimer": "Adaptations are generated solely to optimize learning comfort and engagement."
        }

adaptation_explainer_service = AdaptationExplainerService()
