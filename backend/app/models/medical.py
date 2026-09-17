from pydantic import BaseModel, Field
from typing import List, Optional

class MedicalQuestion(BaseModel):
    id: str
    text: str
    options: List[str]

class MedicalAnswer(BaseModel):
    question_id: str
    question_text: str
    answer: str

class MedicalProfileSubmit(BaseModel):
    learner_id: str
    condition: Optional[str] = "General"
    answers: Optional[List[MedicalAnswer]] = []
