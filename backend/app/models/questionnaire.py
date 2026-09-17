from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class CaregiverQuestionnaireInput(BaseModel):
    """
    20-Question Caretaker Educational Assessment.
    Strictly Non-Diagnostic: Measures observable educational and accessibility needs.
    """
    # 1. Preferred learning environment
    q1_learning_environment: str = Field(
        default="Quiet, distraction-minimized space",
        description="1. Preferred learning environment"
    )
    # 2. Preferred content format
    q2_content_format: str = Field(
        default="Visual diagrams, charts & infographics",
        description="2. Preferred content format"
    )
    # 3. Text tolerance
    q3_text_tolerance: str = Field(
        default="Bite-sized sentences (1 to 2 lines per card)",
        description="3. Text tolerance"
    )
    # 4. Visual support preference
    q4_visual_support: str = Field(
        default="High visual support (diagrams, color coding, icons)",
        description="4. Visual support preference"
    )
    # 5. Audio support preference
    q5_audio_support: str = Field(
        default="On-demand audio button (listen when helpful)",
        description="5. Audio support preference"
    )
    # 6. Pace preference
    q6_pace_preference: str = Field(
        default="Completely untimed, relaxed exploration",
        description="6. Pace preference"
    )
    # 7. Response time
    q7_response_time: str = Field(
        default="Needs extended time to think before answering",
        description="7. Response time"
    )
    # 8. Distraction sensitivity
    q8_distraction_sensitivity: str = Field(
        default="High — visual motion or moving elements break focus",
        description="8. Distraction sensitivity"
    )
    # 9. Content density
    q9_content_density: str = Field(
        default="Single-concept focus (one idea and one action per screen)",
        description="9. Content density"
    )
    # 10. Task chunking
    q10_task_chunking: str = Field(
        default="Micro-challenges (1 to 2 minutes each)",
        description="10. Task chunking"
    )
    # 11. Repetition preference
    q11_repetition_preference: str = Field(
        default="Spiral review (concept revisited with new fresh analogies)",
        description="11. Repetition preference"
    )
    # 12. Instruction complexity
    q12_instruction_complexity: str = Field(
        default="Single-clause direct instructions",
        description="12. Instruction complexity"
    )
    # 13. Difficulty tolerance
    q13_difficulty_tolerance: str = Field(
        default="Prefers high early success with very gradual challenge ramps",
        description="13. Difficulty tolerance"
    )
    # 14. Frustration during repeated errors
    q14_frustration_recovery: str = Field(
        default="Offer a 1-minute calming sensory break or breathing visual",
        description="14. Frustration during repeated errors"
    )
    # 15. Preference for examples
    q15_example_preference: str = Field(
        default="Real-world analogy tied to child's special interest",
        description="15. Preference for examples"
    )
    # 16. Preference for step-by-step guidance
    q16_step_guidance: str = Field(
        default="Always scaffolded (break every question into mini-steps)",
        description="16. Preference for step-by-step guidance"
    )
    # 17. Breaks between activities
    q17_break_frequency: str = Field(
        default="Every 5 to 7 minutes with calm sensory animations",
        description="17. Breaks between activities"
    )
    # 18. Preferred reinforcement style
    q18_reinforcement_style: str = Field(
        default="Visual unlocks (opening new planets, sanctuaries, or cyber parts)",
        description="18. Preferred reinforcement style"
    )
    # 19. Communication/support preference
    q19_support_communication: str = Field(
        default="Warm, patient mentor persona",
        description="19. Communication/support preference"
    )
    # 20. Accessibility or classroom accommodations currently found useful
    q20_accommodations: List[str] = Field(
        default_factory=lambda: [
            "OpenDyslexic font and increased letter spacing",
            "Calm color palette (soft pastels)",
            "Reduced motion (disable auto-sliding and flashing animations)"
        ],
        description="20. Useful accessibility accommodations"
    )

    # Legacy & interest helper fields (for backwards compatibility with existing profiles)
    q1_enjoyed_topics: Optional[str] = ""
    q2_engaging_activities: Optional[str] = ""
    q3_themes: Optional[List[str]] = Field(default_factory=lambda: ["Space", "Animals"])
    q4_hobbies: Optional[str] = ""
    q5_voluntary_subjects: Optional[str] = ""
    q6_favorite_color: Optional[str] = "blue"
    q7_disliked_colors: Optional[List[str]] = Field(default_factory=list)
    q8_color_palette_preference: Optional[str] = "soft"
    q9_visual_style_preference: Optional[str] = "mixture"
    q10_animation_effect: Optional[str] = "distract"
    q11_sound_effect: Optional[str] = "distract"
    q12_prefer_calm_screen: Optional[bool] = True
    q13_prefer_movement: Optional[bool] = False
    q14_avoided_patterns: Optional[str] = ""
    q15_learning_modality: Optional[List[str]] = Field(default_factory=lambda: ["Seeing", "Doing"])
    q16_task_structure: Optional[str] = "step_by_step"
    q17_difficulty_reaction: Optional[str] = "needs_break"
    q18_reengagement_helper: Optional[str] = "visual_reward"
    q19_feedback_style: Optional[str] = "immediate"
    q20_excitement_triggers: Optional[str] = ""
    q21_reward_types: Optional[List[str]] = Field(default_factory=lambda: ["Unlocking something", "Collecting objects"])
    q22_frustration_triggers: Optional[str] = ""
    q23_calming_methods: Optional[str] = ""
    q24_platform_avoidances: Optional[str] = ""

class CaregiverQuestionnaireResponse(CaregiverQuestionnaireInput):
    id: str
    caregiver_id: str
    learner_id: str
    created_at: datetime
