import logging
from typing import Dict, Any, List, Optional
from app.services.ai_mentor import ai_mentor_service

logger = logging.getLogger("neuroquest.scaffold_engine")

class ScaffoldEngine:
    """Manages low-stress failure scaffolding and representation switching for neurodivergent learners."""

    async def get_scaffold_response(
        self,
        task: Dict[str, Any],
        attempt_count: int,
        learner_context: Dict[str, Any]
    ) -> Dict[str, Any]:

        question = task.get("question", "")
        correct_answer = task.get("correct_answer", "")
        hints = task.get("hints", [])
        
        # 1. Gentle Non-Punitive Feedback Message
        feedback_messages = [
            "Let's try another route together!",
            "Good exploration effort! Here is a helpful clue.",
            "You are doing great. Let's look at this step from a new perspective.",
            "Learning is an adventure — take your time!"
        ]
        chosen_message = feedback_messages[(attempt_count - 1) % len(feedback_messages)]

        # 2. Representation & Scaffolding Strategy
        next_representation = "standard"
        action = "hint"
        scaffold_step = None

        if attempt_count == 1:
            action = "hint"
            hint_text = hints[0] if hints else await ai_mentor_service.generate_gentle_hint(question, correct_answer, learner_context, 1)

        elif attempt_count == 2:
            action = "change_representation"
            next_representation = "visual_block" # Switch to visual blocks / diagram representation
            hint_text = "Visual Clue: Imagine grouping the items into equal blocks!"

        else: # 3+ attempts
            action = "scaffold_and_reduce"
            next_representation = "simplified"
            hint_text = f"Simplified Example: If we take 1 group of {correct_answer}, the result is {correct_answer}!"
            scaffold_step = {
                "step_title": "Bite-sized Step",
                "simplified_prompt": f"Which of these matches {correct_answer}?",
                "suggested_answer": correct_answer
            }

        return {
            "feedback_message": chosen_message,
            "action": action,
            "next_representation": next_representation,
            "hint": hint_text,
            "scaffold_step": scaffold_step,
            "should_modify_strategy": attempt_count >= 2
        }

scaffold_engine = ScaffoldEngine()
