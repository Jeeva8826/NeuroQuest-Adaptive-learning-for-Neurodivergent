from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class MasteryNode(BaseModel):
    id: str
    subject: str
    title: str
    level: int = 1
    is_unlocked: bool = False
    is_completed: bool = False
    icon: str = "Star"
    parent_id: Optional[str] = None

class PersonalMasteryTree(BaseModel):
    learner_id: str
    nodes: List[MasteryNode] = Field(default_factory=list)
    completion_percentage: float = 0.0

class ExplorationNode(BaseModel):
    id: str
    name: str
    description: str
    theme: str # space, animals, sports, art, coding, music, cars, fantasy
    is_unlocked: bool = False
    is_current: bool = False
    milestones_required: int = 1
    unlocked_at: Optional[datetime] = None

class InventoryItem(BaseModel):
    id: str
    name: str
    item_type: str # collectible, building_module, avatar_item, story_chapter, tool
    description: str
    icon: str
    theme: str
    acquired_at: datetime = Field(default_factory=datetime.utcnow)

class PersonalGameWorld(BaseModel):
    learner_id: str
    world_name: str = "Cosmic Sanctuary"
    theme: str = "space"
    hero_role: str = "Explorer"
    active_zone: str = "Space Station Dock"
    unlocked_zones: List[str] = Field(default_factory=lambda: ["Space Station Dock"])
    exploration_map: List[ExplorationNode] = Field(default_factory=list)
    inventory: List[InventoryItem] = Field(default_factory=list)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
