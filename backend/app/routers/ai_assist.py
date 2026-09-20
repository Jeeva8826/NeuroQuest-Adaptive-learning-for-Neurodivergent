from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from app.services.auth_service import get_current_user, get_optional_current_user
from app.services.llm_service import generate_adaptive_explanation
from app.services.scaffold_engine import scaffold_engine
from app.services.rag_service import rag_service
from app.services.student_answer_evaluator import student_answer_evaluator

router = APIRouter(prefix="/api/ai", tags=["AI Assistance"])

class AIExplainRequest(BaseModel):
    question: str
    correct_answer: str
    learner_interests: Optional[List[str]] = None
    guidance_level: Optional[str] = "high"

class ContextualAssistRequest(BaseModel):
    user_message: str = Field(..., description="Student query or clarification request")
    task: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Current curriculum task object")
    task_id: Optional[str] = None
    scaffold_level: Optional[int] = Field(None, ge=0, le=5, description="Current scaffold ladder level (0 to 5)")
    attempt_count: int = Field(1, ge=0, description="Current question attempt count")
    learner_interests: Optional[List[str]] = Field(default_factory=lambda: ["space"], description="Student interests for analogies")

class AnswerEvaluationRequest(BaseModel):
    question: str
    student_answer: str
    correct_answer: str
    options: Optional[List[str]] = None
    concept_id: Optional[str] = None
    learner_interests: Optional[List[str]] = None

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

@router.post("/contextual-assist")
@router.post("/assistant")
async def contextual_ai_assistant(
    req: ContextualAssistRequest,
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Contextual AI Assistant connected to the 6-Level Scaffolding Engine and PGVector RAG Pipeline.
    Strictly prevents premature answer leakage before Level 5 while providing NCERT-grounded
    pedagogical assistance customized to the student's current scaffolding ladder level.
    """
    task = req.task or {}
    q_text = task.get("question") or task.get("prompt") or req.user_message
    correct_ans = task.get("correct_answer", "")
    interests = req.learner_interests or ["space"]
    primary_interest = interests[0].lower() if interests else "space"

    # 1. Retrieve current 6-Level scaffold state
    learner_context = {"interests": interests}
    scaffold_state = await scaffold_engine.get_scaffold_response(
        task=task if task else {"question": q_text, "correct_answer": correct_ans},
        attempt_count=req.attempt_count,
        learner_context=learner_context,
        requested_level=req.scaffold_level
    )
    curr_level = scaffold_state["scaffold_level"]

    # 2. Retrieve grounded NCERT knowledge chunk via RAG
    rag_hits = rag_service.search(f"{q_text} {req.user_message}", top_k=2)
    citation = rag_hits[0]["citation"] if rag_hits else "NCERT Curriculum Framework"
    concept_name = rag_hits[0].get("concept_name", "Core Concept") if rag_hits else "Concept"

    # 3. Formulate safe, non-leaking assistant reply based on current scaffold level
    if curr_level == 0:
        # Level 0: Clarifying Question
        reply = (
            f"Hello fellow explorer! Let's clarify what this mission is asking first: "
            f"{scaffold_state.get('clarifying_question') or scaffold_state['hint']} "
            f"Think about what property of '{concept_name}' is most important here."
        )
        safety_status = "level_0_clarifying_prompt"

    elif curr_level == 1:
        # Level 1: Hint
        reply = (
            f"Here's a gentle hint to guide your thinking: {scaffold_state['hint']} "
            f"Notice how this connects to {primary_interest} — look closely at the clues in the question!"
        )
        safety_status = "level_1_gentle_hint"

    elif curr_level == 2:
        # Level 2: Concept Explanation
        concept_clue = scaffold_state.get("concept_explanation") or scaffold_state["hint"]
        reply = (
            f"Let's look at the underlying principle from {citation}: {concept_clue} "
            f"We've switched to visual blocks and ruled out distractors to keep things clear!"
        )
        safety_status = "level_2_concept_explanation"

    elif curr_level == 3:
        # Level 3: Example
        ex = scaffold_state.get("worked_example") or {}
        scenario = ex.get("scenario", "a parallel scenario")
        solution = ex.get("solution", "the pattern holds")
        reply = (
            f"Here is a parallel example to show how the rule works: {scenario}. "
            f"In that case, the result is: {solution}. "
            f"Can you apply that exact same logic to our current question?"
        )
        safety_status = "level_3_worked_example"

    elif curr_level == 4:
        # Level 4: Step-by-Step Guidance
        steps = scaffold_state.get("reasoning_walkthrough", [])
        steps_str = " -> ".join(steps[:2]) if steps else scaffold_state['hint']
        reply = (
            f"You are super close! Let's take the partial step together: {steps_str}. "
            f"Now, what is the final choice that completes this pattern?"
        )
        safety_status = "level_4_partial_step"

    else:
        # Level 5: Full Explanation (Complete breakdown)
        full_sol = scaffold_state.get("full_solution") or {}
        sol_text = full_sol.get("explanation", scaffold_state["hint"])
        ans_text = full_sol.get("final_answer", correct_ans)
        reply = (
            f"Fantastic perseverance exploring all the way through! "
            f"The complete solution is '{ans_text}'. "
            f"Here is why: {sol_text} "
            f"Every great scientist learns by testing hypotheses — you've mastered this concept!"
        )
        safety_status = "level_5_full_explanation_authorized"

    return {
        "assistant_reply": reply,
        "scaffold_level": curr_level,
        "level_name": scaffold_state["level_name"],
        "ladder_progress": scaffold_state["ladder_progress"],
        "citation": citation,
        "evidence_chunks": rag_hits,
        "safety_check": safety_status,
        "can_advance_scaffold": curr_level < 5
    }

@router.post("/evaluate-answer")
async def evaluate_answer_endpoint(
    req: AnswerEvaluationRequest,
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Evaluates a student's answer using the structured StudentAnswerEvaluator.
    Returns: status, reason, misconception, correct_concept, feedback, next_step.
    """
    result = student_answer_evaluator.evaluate_answer(
        question=req.question,
        student_answer=req.student_answer,
        correct_answer=req.correct_answer,
        options=req.options,
        concept_id=req.concept_id,
        learner_context={"interests": req.learner_interests or ["space"]}
    )
    return result
