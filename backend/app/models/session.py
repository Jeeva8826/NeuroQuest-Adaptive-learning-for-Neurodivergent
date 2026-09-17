from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class TaskAnswerSubmit(BaseModel):
    task_id: str
    selected_answer: str
    time_taken_seconds: int = 0
    hints_used: int = 0

class LearningEvent(BaseModel):
    learner_id: str
    session_id: str
    event_type: str # task_start, answer_submit, hint_requested, break_taken, feedback_received
    payload: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class LearnerSession(BaseModel):
    id: Optional[str] = None
    learner_id: str
    started_at: datetime = Field(default_factory=datetime.utcnow)
    ended_at: Optional[datetime] = None
    tasks_completed: int = 0
    correct_count: int = 0
    points_earned: int = 0
    subject_summary: Dict[str, int] = Field(default_factory=dict)
    status: str = "active" # active, completed
