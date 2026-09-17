import logging
from typing import Dict, Any, List
from app.services.ai_mentor import ai_mentor_service
from app.services.interest_engine import interest_engine

logger = logging.getLogger("neuroquest.daily_experience")

class DailyExperienceService:
    """Generates a personalized daily return experience instead of generic streaks."""

    async def construct_daily_experience(
        self,
        learner_profile: Dict[str, Any],
        previous_session: Dict[str, Any] = None,
        recent_progress: Dict[str, Any] = None
    ) -> Dict[str, Any]:

        learner_name = learner_profile.get("learner_name", "Learner")
        interests = learner_profile.get("interests", ["space"])
        theme_data = interest_engine.resolve_theme(interests)

        # Context for AI Mentor
        learner_context = {
            "interests": interests,
            "preferredLearningMode": learner_profile.get("preferred_learning_modes", ["visual"])[0] if learner_profile.get("preferred_learning_modes") else "visual",
            "currentState": "FOCUSED",
            "difficulty": 1
        }

        perf_summary = {
            "last_session_tasks": previous_session.get("tasks_completed", 0) if previous_session else 0,
            "last_session_correct": previous_session.get("correct_count", 0) if previous_session else 0,
            "total_stars": recent_progress.get("total_stars", 10) if recent_progress else 10
        }

        ai_welcome = await ai_mentor_service.generate_daily_welcome_mission(
            learner_name=learner_name,
            learner_context=learner_context,
            recent_performance=perf_summary
        )

        return {
            "greeting": ai_welcome["greeting"],
            "mission_title": ai_welcome["mission_title"],
            "world_name": theme_data["world_name"],
            "hero_role": theme_data["hero_role"],
            "active_zone": theme_data["zones"][0],
            "theme": theme_data["theme_id"],
            "primary_color": theme_data["primary_color"],
            "secondary_color": theme_data["secondary_color"]
        }

daily_experience_service = DailyExperienceService()
