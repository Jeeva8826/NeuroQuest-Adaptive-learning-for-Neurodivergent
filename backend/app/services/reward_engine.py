import logging
from typing import Dict, Any, List
from datetime import datetime
from app.models.game_world import InventoryItem, ExplorationNode
from app.services.interest_engine import interest_engine

logger = logging.getLogger("neuroquest.reward_engine")

class RewardEngine:
    """Delivers personalized rewards aligned with learner motivation types."""

    def evaluate_task_reward(
        self,
        learner_id: str,
        gamification_profile: Dict[str, Any],
        learner_interests: List[str],
        task_subject: str,
        is_correct: bool,
        current_world_state: Dict[str, Any] = None
    ) -> Dict[str, Any]:

        theme_data = interest_engine.resolve_theme(learner_interests)
        motivation_types = gamification_profile.get("motivation_types", ["exploration", "collection"])
        primary_motivation = motivation_types[0] if motivation_types else "exploration"

        reward_type = "collectible"
        item_unlocked = None
        message = "Awesome progress!"
        zone_unlocked = None

        if primary_motivation == "exploration":
            reward_type = "exploration_node"
            next_zone = theme_data["zones"][(len(current_world_state.get("unlocked_zones", [])) % len(theme_data["zones"]))] if current_world_state else theme_data["zones"][0]
            zone_unlocked = next_zone
            message = f"🌟 You've unlocked a new area: {next_zone}!"

        elif primary_motivation == "collection":
            reward_type = "collectible"
            col_name = theme_data["collectible_types"][(len(current_world_state.get("inventory", [])) % len(theme_data["collectible_types"]))] if current_world_state else theme_data["collectible_types"][0]
            item_unlocked = InventoryItem(
                id=f"col_{int(datetime.utcnow().timestamp())}",
                name=col_name,
                item_type="collectible",
                description=f"A rare item unlocked during your {theme_data['world_name']} quest.",
                icon="Award",
                theme=theme_data["theme_id"]
            )
            message = f"🏆 Collected: {col_name}!"

        elif primary_motivation == "building":
            reward_type = "building_component"
            comp_name = f"{theme_data['hero_role']} Module Part"
            item_unlocked = InventoryItem(
                id=f"build_{int(datetime.utcnow().timestamp())}",
                name=comp_name,
                item_type="building_module",
                description="Use this module component to expand your personal workshop.",
                icon="Cpu",
                theme=theme_data["theme_id"]
            )
            message = f"🛠️ Workshop Unlocked: {comp_name}!"

        elif primary_motivation == "customization":
            reward_type = "customization"
            item_unlocked = InventoryItem(
                id=f"cust_{int(datetime.utcnow().timestamp())}",
                name=f"{theme_data['theme_id'].capitalize()} Theme Color Badge",
                item_type="avatar_item",
                description="New accent color unlocked for your custom interface banner.",
                icon="Palette",
                theme=theme_data["theme_id"]
            )
            message = "🎨 Unlocked new theme customization options!"

        elif primary_motivation == "story":
            reward_type = "story_chapter"
            item_unlocked = InventoryItem(
                id=f"story_{int(datetime.utcnow().timestamp())}",
                name=f"Chapter {len(current_world_state.get('inventory', [])) + 1}: The {theme_data['hero_role']}'s Journey",
                item_type="story_chapter",
                description=f"You unlocked the next story log in {theme_data['world_name']}!",
                icon="BookOpen",
                theme=theme_data["theme_id"]
            )
            message = "📖 New Story Chapter Unlocked!"

        else: # mastery / discovery / default
            reward_type = "mastery_leaf"
            message = f"✨ Mastery Node Advanced in {task_subject}!"

        return {
            "reward_type": reward_type,
            "message": message,
            "item_unlocked": item_unlocked.model_dump() if item_unlocked else None,
            "zone_unlocked": zone_unlocked,
            "stars_earned": 10 if is_correct else 2 # secondary optional non-intrusive metric
        }

reward_engine = RewardEngine()
