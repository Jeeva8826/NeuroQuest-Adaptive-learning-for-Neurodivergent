from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from app.services.auth_service import get_current_user
from app.services.llm_service import generate_adaptive_explanation

router = APIRouter(prefix="/api/ai", tags=["AI Assistance"])

class AIExplainRequest(BaseModel):
    question: str
    correct_answer: str
    learner_interests: Optional[List[str]] = None
    guidance_level: Optional[str] = "high"

@router.post("/explain")
async def get_adaptive_explanation(
    req: AIExplainRequest,
    current_user: dict = Depends(get_current_user)
):
    explanation = await generate_adaptive_explanation(
        question=req.question,
        correct_answer=req.correct_answer,
        learner_interests=req.learner_interests,
        guidance_level=req.guidance_level
    )
    return {"explanation": explanation}
