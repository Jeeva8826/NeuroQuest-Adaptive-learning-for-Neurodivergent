from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class StepGuide(BaseModel):
    step_number: int
    title: str
    description: str
    hint: Optional[str] = None

class MicroMilestone(BaseModel):
    milestone_id: str
    title: str
    question: str
    options: List[str] = Field(default_factory=list)
    correct_answer: str
    explanation: str
    hint: Optional[str] = None

class LearningTask(BaseModel):
    id: Optional[str] = None
    title: str
    subject: str # Mathematics, Science, English, General Knowledge, Coding/Logic
    difficulty: int = 1 # 1 to 5
    estimated_duration: int = 5 # minutes
    
    question: str
    content_type: str = "multiple_choice" # multiple_choice, step_by_step, text_input, drag_or_select
    options: List[str] = Field(default_factory=list)
    correct_answer: str
    explanation: str
    
    hints: List[str] = Field(default_factory=list)
    steps: List[StepGuide] = Field(default_factory=list)
    milestone_steps: List[MicroMilestone] = Field(default_factory=list)
    
    mission_context: Optional[str] = None # Personalized mission narrative
    representation_type: str = "standard" # standard, visual_block, audio_supported, simplified
    
    supported_learning_modes: List[str] = Field(default_factory=lambda: ["Seeing", "Doing"])
    theme_tags: List[str] = Field(default_factory=lambda: ["space", "animals", "coding", "general"])
    
    icon_name: str = "BookOpen"

