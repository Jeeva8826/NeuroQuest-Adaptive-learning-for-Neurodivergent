from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class CaregiverQuestionnaireInput(BaseModel):
    # INTERESTS (Q1 - Q5)
    q1_enjoyed_topics: str = Field("", description="Topics the learner naturally enjoys talking about")
    q2_engaging_activities: str = Field("", description="Activities they spend a long time doing willingly")
    q3_themes: List[str] = Field(default_factory=list, description="Themes that attract them: Space, Animals, Cars, Sports, Art, Music, Coding/Technology, Nature, Fantasy, Games, Stories, Other")
    q4_hobbies: str = Field("", description="Current favorite hobbies")
    q5_voluntary_subjects: str = Field("", description="Subjects they voluntarily explore")

    # VISUAL PREFERENCES (Q6 - Q9)
    q6_favorite_color: str = Field("blue", description="Favorite color")
    q7_disliked_colors: List[str] = Field(default_factory=list, description="Colors usually disliked or avoided")
    q8_color_palette_preference: str = Field("soft", description="Bright colors, Soft/muted colors, Dark themes, High contrast, Minimal colors")
    q9_visual_style_preference: str = Field("mixture", description="Pictures, Icons, Diagrams, Text, A mixture")

    # SENSORY PREFERENCES (Q10 - Q14)
    q10_animation_effect: str = Field("distract", description="Do animations help or distract? (help, distract, neutral)")
    q11_sound_effect: str = Field("distract", description="Do sounds help focus or distract? (help, distract, neutral)")
    q12_prefer_calm_screen: bool = Field(True, description="Prefer visually calm screen?")
    q13_prefer_movement: bool = Field(False, description="Prefer movement/interaction?")
    q14_avoided_patterns: str = Field("", description="Visual patterns/colors avoided")

    # LEARNING PREFERENCES (Q15 - Q19)
    q15_learning_modality: List[str] = Field(default_factory=lambda: ["Seeing", "Doing"], description="Seeing, Listening, Doing, Reading, Combination")
    q16_task_structure: str = Field("step_by_step", description="Small tasks, Longer challenges, Step-by-step guidance, Exploration")
    q17_difficulty_reaction: str = Field("needs_break", description="Reaction when task becomes difficult")
    q18_reengagement_helper: str = Field("visual_reward", description="What helps return to task after losing interest")
    q19_feedback_style: str = Field("immediate", description="Immediate feedback or after completing task")

    # MOTIVATION (Q20 - Q21)
    q20_excitement_triggers: str = Field("", description="What makes them excited to complete activity")
    q21_reward_types: List[str] = Field(default_factory=list, description="Unlocking something, Collecting objects, Exploring, Building, Stories, Characters, Music/sounds, Visual effects, Choice/control, Praise/encouragement, Other")

    # COMFORT & FRUSTRATION (Q22 - Q24)
    q22_frustration_triggers: str = Field("", description="What usually makes learning frustrating")
    q23_calming_methods: str = Field("", description="What usually helps calm them")
    q24_platform_avoidances: str = Field("", description="What should the platform avoid")

class CaregiverQuestionnaireResponse(CaregiverQuestionnaireInput):
    id: str
    caregiver_id: str
    learner_id: str
    created_at: datetime
