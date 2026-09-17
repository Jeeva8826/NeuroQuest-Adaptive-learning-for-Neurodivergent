from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class RewardBadge(BaseModel):
    id: str
    title: str
    description: str
    icon: str
    unlocked_at: Optional[datetime] = None
    is_unlocked: bool = False
    category: str = "achievement"

class LearnerProgress(BaseModel):
    learner_id: str
    total_stars: int = 0
    total_tasks_completed: int = 0
    streak_days: int = 1
    subject_mastery: Dict[str, int] = Field(default_factory=lambda: {
        "Mathematics": 0,
        "Science": 0,
        "English": 0,
        "General Knowledge": 0,
        "Coding/Logic": 0
    })
    earned_badges: List[RewardBadge] = Field(default_factory=list)
    unlocked_themes: List[str] = Field(default_factory=lambda: ["space", "animals"])
    last_active: datetime = Field(default_factory=datetime.utcnow)
