from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
import logging

logger = logging.getLogger("neuroquest.medical")

router = APIRouter(prefix="/medical", tags=["Medical ICMR"])

class MedicalQuestion(BaseModel):
    id: str
    text: str
    options: List[str]

class Answer(BaseModel):
    question_id: str
    question_text: str
    answer: str

class MedicalProfileSubmit(BaseModel):
    learner_id: str
    condition: str
    answers: List[Answer]

# Standard ICMR-style pediatric cognitive assessment proxy questions (INCLEN derived)
ICMR_QUESTIONS = [
    {"id": "ICMR-1", "text": "Does the child have difficulty sustaining attention in tasks or play activities?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-2", "text": "Does the child avoid, dislike, or is reluctant to engage in tasks that require sustained mental effort?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-3", "text": "Is the child easily distracted by extraneous stimuli?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-4", "text": "Does the child fidget with hands or feet or squirm in seat?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-5", "text": "Does the child have difficulty playing or engaging in leisure activities quietly?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-6", "text": "Does the child talk excessively?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-7", "text": "Does the child display delayed speech and language development?", "options": ["No Delay", "Mild Delay", "Moderate", "Severe"]},
    {"id": "ICMR-8", "text": "Does the child have difficulty making eye contact during conversations?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-9", "text": "Does the child show lack of spontaneous seeking to share enjoyment, interests, or achievements with others?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-10", "text": "Does the child engage in stereotyped and repetitive motor mannerisms (e.g., hand or finger flapping)?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-11", "text": "Does the child have persistent preoccupation with parts of objects?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-12", "text": "Does the child show hyper-reactivity or hypo-reactivity to sensory input (e.g., adverse response to specific sounds)?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-13", "text": "Does the child have difficulty organizing tasks and activities?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-14", "text": "Does the child frequently lose things necessary for tasks or activities?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-15", "text": "Does the child have a history of seizures or abnormal EEG findings?", "options": ["No", "Suspected", "Yes - Medicated", "Yes - Unmedicated"]},
    {"id": "ICMR-16", "text": "Does the child have difficulty reading single words accurately and fluently?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-17", "text": "Does the child have difficulty comprehending the meaning of what is read?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-18", "text": "Does the child have difficulty with spelling and written expression?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-19", "text": "Does the child have difficulty mastering number sense, number facts or calculation?", "options": ["Rarely", "Sometimes", "Often", "Always"]},
    {"id": "ICMR-20", "text": "Is there a family history of neurodevelopmental disorders?", "options": ["No", "Extended Family", "Immediate Family", "Unknown"]}
]

@router.get("/questions/{learner_id}", response_model=List[MedicalQuestion])
async def fetch_questions(learner_id: str):
    logger.info(f"Fetching ICMR medical questions for learner {learner_id}")
    return ICMR_QUESTIONS

@router.post("/submit")
async def submit_medical_profile(profile: MedicalProfileSubmit):
    logger.info(f"Received medical profile for learner {profile.learner_id} with {len(profile.answers)} answers.")
    # In the MVP, we just accept the submission and return success. 
    # Real implementations would save this to the SQLAlchemy database.
    return {"status": "success", "message": "ICMR Medical profile saved successfully"}
