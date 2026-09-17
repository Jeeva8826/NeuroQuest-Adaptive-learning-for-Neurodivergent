import logging
from typing import Dict, Any, List
from datetime import datetime
from app.database import get_database
from app.models.game_world import PersonalGameWorld, PersonalMasteryTree, MasteryNode, ExplorationNode, InventoryItem
from app.services.interest_engine import interest_engine

logger = logging.getLogger("neuroquest.game_world_service")

class GameWorldService:
    """Manages the learner's personal game world, non-competitive mastery tree, and exploration map."""

    async def get_or_create_game_world(self, learner_id: str, learner_profile: Dict[str, Any]) -> Dict[str, Any]:
        db = get_database()
        world_doc = await db["personal_game_worlds"].find_one({"learner_id": learner_id})
        
        interests = learner_profile.get("interests", ["space"])
        theme_data = interest_engine.resolve_theme(interests)

        if not world_doc:
            # Build initial exploration nodes based on theme
            nodes = [
                ExplorationNode(
                    id=f"zone_{i}",
                    name=zone,
                    description=f"Explore the {zone} in your {theme_data['world_name']}.",
                    theme=theme_data["theme_id"],
                    is_unlocked=(i == 0),
                    is_current=(i == 0),
                    milestones_required=i + 1
                )
                for i, zone in enumerate(theme_data["zones"])
            ]

            init_item = InventoryItem(
                id="init_badge_1",
                name=f"{theme_data['hero_role']} Badge",
                item_type="collectible",
                description=f"Official badge of the {theme_data['hero_role']}.",
                icon="Award",
                theme=theme_data["theme_id"]
            )

            world_obj = PersonalGameWorld(
                learner_id=learner_id,
                world_name=theme_data["world_name"],
                theme=theme_data["theme_id"],
                hero_role=theme_data["hero_role"],
                active_zone=theme_data["zones"][0],
                unlocked_zones=[theme_data["zones"][0]],
                exploration_map=nodes,
                inventory=[init_item]
            )

            world_doc = world_obj.model_dump()
            await db["personal_game_worlds"].insert_one(world_doc)

        return world_doc

    async def get_or_create_mastery_tree(self, learner_id: str) -> Dict[str, Any]:
        db = get_database()
        tree_doc = await db["personal_mastery_trees"].find_one({"learner_id": learner_id})

        if not tree_doc:
            subjects = ["Mathematics", "Science", "English", "Coding/Logic", "General Knowledge"]
            nodes = []
            for sub in subjects:
                nodes.append(MasteryNode(id=f"{sub.lower()}_1", subject=sub, title=f"{sub} Basics", level=1, is_unlocked=True, is_completed=False, icon="BookOpen"))
                nodes.append(MasteryNode(id=f"{sub.lower()}_2", subject=sub, title=f"{sub} Explorer", level=2, is_unlocked=False, is_completed=False, icon="Star", parent_id=f"{sub.lower()}_1"))
                nodes.append(MasteryNode(id=f"{sub.lower()}_3", subject=sub, title=f"{sub} Master", level=3, is_unlocked=False, is_completed=False, icon="Award", parent_id=f"{sub.lower()}_2"))

            tree_obj = PersonalMasteryTree(learner_id=learner_id, nodes=nodes, completion_percentage=10.0)
            tree_doc = tree_obj.model_dump()
            await db["personal_mastery_trees"].insert_one(tree_doc)

        return tree_doc

game_world_service = GameWorldService()
