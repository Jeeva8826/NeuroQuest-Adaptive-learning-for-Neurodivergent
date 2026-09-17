from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class VisualPreferences(BaseModel):
    favorite_colors: List[str] = Field(default_factory=list)
    avoided_colors: List[str] = Field(default_factory=list)
    palette_type: str = "soft" # bright, soft, dark, high_contrast, minimal
    visual_style: str = "mixture" # pictures, icons, diagrams, text, mixture
    primary_color: str = "#3b82f6"
    secondary_color: str = "#8b5cf6"
    background_theme: str = "space" # space, animals, coding, nature, fantasy, art, music, sports
    font_family: str = "sans" # sans, rounded, dyslexic
    font_scale: str = "medium" # small, medium, large, xlarge

class SensoryPreferences(BaseModel):
    sound_enabled: bool = False
    sound_preference: str = "quiet" # quiet, calm_chimes, positive_pings
    animation_intensity: str = "low" # none, low, normal, high
    visual_density: str = "spacious" # spacious, balanced, compact
    calm_mode: bool = True

class MotivationPreferences(BaseModel):
    preferred_rewards: List[str] = Field(default_factory=list)
    reward_style: str = "badges_unlocks" # badges_unlocks, collectables, exploration, celebration

class GamificationProfile(BaseModel):
    motivation_types: List[str] = Field(default_factory=lambda: ["exploration", "collection"])
    game_theme: str = "space"
    reward_preference: str = "unlockables" # unlockables, collectibles, components, avatar_items, story_chapters, tools
    interaction_preference: str = "step_by_step"
    celebration_preference: str = "gentle_sparkles" # quiet, gentle_sparkles, sound_chime, visual_banner
    progress_style: str = "mastery_tree" # mastery_tree, exploration_map, quest_journey

class InteractionPreferences(BaseModel):
    task_size: str = "small" # small, medium, large
    feedback_style: str = "immediate" # immediate, summary
    guidance_level: str = "high" # high (step-by-step), moderate, low (exploration)
    break_frequency_mins: int = 10

class LearnerProfile(BaseModel):
    id: Optional[str] = None
    learner_id: str
    caregiver_id: str
    learner_name: str = "Learner"
    learner_age: Optional[int] = None
    
    interests: List[str] = Field(default_factory=list)
    hobbies: List[str] = Field(default_factory=list)
    preferred_learning_modes: List[str] = Field(default_factory=list)
    
    visual_preferences: VisualPreferences = Field(default_factory=VisualPreferences)
    sensory_preferences: SensoryPreferences = Field(default_factory=SensoryPreferences)
    motivation: MotivationPreferences = Field(default_factory=MotivationPreferences)
    gamification: GamificationProfile = Field(default_factory=GamificationProfile)
    interaction_preferences: InteractionPreferences = Field(default_factory=InteractionPreferences)
    
    avoidance_keywords: List[str] = Field(default_factory=list)
    calming_strategies: List[str] = Field(default_factory=list)
    
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class PreferenceUpdateRequest(BaseModel):
    primary_color: Optional[str] = None
    secondary_color: Optional[str] = None
    palette_type: Optional[str] = None
    background_theme: Optional[str] = None
    font_family: Optional[str] = None
    font_scale: Optional[str] = None
    animation_intensity: Optional[str] = None
    sound_enabled: Optional[bool] = None
    visual_density: Optional[str] = None
    task_size: Optional[str] = None
    guidance_level: Optional[str] = None
    motivation_types: Optional[List[str]] = None
    game_theme: Optional[str] = None
    reward_preference: Optional[str] = None

