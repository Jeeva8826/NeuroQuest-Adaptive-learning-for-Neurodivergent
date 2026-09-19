import os
import json
import logging
from typing import Dict, Any, List, Optional
from app.services.ai_mentor import ai_mentor_service

logger = logging.getLogger("neuroquest.scaffold_engine")

# Load and index NCERT curriculum knowledge graph for grounded pedagogical scaffolding
NCERT_KG: Dict[str, Any] = {}
CONCEPTS_BY_ID: Dict[str, Any] = {}
QUESTIONS_BY_ID: Dict[str, Any] = {}

def _init_ncert_cache():
    global NCERT_KG, CONCEPTS_BY_ID, QUESTIONS_BY_ID
    if CONCEPTS_BY_ID:
        return
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        kg_path = os.path.normpath(os.path.join(base_dir, "..", "..", "..", "data", "curriculum", "ncert_knowledge_graph.json"))
        if os.path.exists(kg_path):
            with open(kg_path, "r", encoding="utf-8") as f:
                NCERT_KG = json.load(f)
            for sub in NCERT_KG.get("subjects", []):
                for ch in sub.get("chapters", []):
                    for top in ch.get("topics", []):
                        for con in top.get("concepts", []):
                            c_id = con.get("concept_id")
                            if c_id:
                                CONCEPTS_BY_ID[c_id] = {**con, "subject": sub.get("subject_name"), "chapter": ch.get("title"), "grade": ch.get("grade"), "standard": ch.get("standard")}
                            for q in con.get("questions", []):
                                q_id = q.get("question_id")
                                if q_id:
                                    QUESTIONS_BY_ID[q_id] = {**q, "concept_id": c_id, "subject": sub.get("subject_name"), "grade": ch.get("grade"), "standard": ch.get("standard")}
            logger.info(f"ScaffoldEngine indexed {len(CONCEPTS_BY_ID)} NCERT concepts & {len(QUESTIONS_BY_ID)} curriculum questions across all standards.")
    except Exception as e:
        logger.warning(f"Could not index NCERT Knowledge Graph in ScaffoldEngine: {e}")

_init_ncert_cache()

class ScaffoldEngine:
    """
    Manages low-stress, non-punitive failure scaffolding with a graduated 7-Level Ladder.
    Grounded in NCERT curriculum knowledge graph and learner-selected interests.
    
    Level 1: Restate goal simply (in learner's interest domain)
    Level 2: Highlight key concept / eliminate 1 wrong option
    Level 3: Guiding question (Socratic nudge)
    Level 4: Small worked example (analogous numbers/scenarios)
    Level 5: Partial steps (fill-in-the-blank)
    Level 6: Explain reasoning without giving away final answer
    Level 7: Full solution with step-by-step breakdown (only when requested or max attempts exceeded)
    """

    def _find_concept_context(self, task: Dict[str, Any]) -> Dict[str, Any]:
        _init_ncert_cache()
        task_id = str(task.get("id", ""))
        concept_id = task.get("concept_id")

        if concept_id and concept_id in CONCEPTS_BY_ID:
            return CONCEPTS_BY_ID[concept_id]

        if task_id and task_id in QUESTIONS_BY_ID:
            c_id = QUESTIONS_BY_ID[task_id].get("concept_id")
            if c_id in CONCEPTS_BY_ID:
                return CONCEPTS_BY_ID[c_id]

        # Keyword match from question prompt
        question_text = str(task.get("question", "")).lower()
        for cid, con in CONCEPTS_BY_ID.items():
            cname = con.get("concept_name", "").lower()
            if cname in question_text or any(word in question_text for word in cname.split() if len(word) > 4):
                return con

        return {}

    async def get_scaffold_response(
        self,
        task: Dict[str, Any],
        attempt_count: int,
        learner_context: Dict[str, Any],
        requested_level: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generates a graduated 7-level scaffold step tailored to learner needs.
        Preserves complete backwards compatibility with legacy tests.
        """
        question = task.get("question") or task.get("prompt", "")
        correct_answer = str(task.get("correct_answer", ""))
        options = task.get("options", [])
        hints = task.get("hints", [])
        scaffold_steps = task.get("scaffold_steps", [])
        explanation = task.get("explanation", "")

        interests = learner_context.get("interests", ["space"])
        primary_interest = str(interests[0]).lower() if interests else "space"

        # Determine scaffolding level (1 to 7)
        if requested_level is not None:
            level = max(1, min(7, int(requested_level)))
        else:
            level = max(1, min(7, attempt_count))

        concept_data = self._find_concept_context(task)
        interest_analogies = concept_data.get("explanation", {}).get("interest_analogies", {})
        analogy_text = (
            interest_analogies.get(primary_interest)
            or interest_analogies.get("space")
            or concept_data.get("explanation", {}).get("simplified")
            or ""
        )
        misconceptions = concept_data.get("misconceptions", [])
        misconception_truth = misconceptions[0].get("scientific_truth") if misconceptions else ""

        # Non-punitive encouraging feedback messages
        feedback_messages = {
            1: "Let's take a deep breath — here is a clear look at our goal!",
            2: "Good exploration effort! Let's eliminate a distractor with a visual clue.",
            3: "You are doing great! Let's think through this guiding question together.",
            4: "Here is a quick parallel example to show how the pattern works!",
            5: "Almost there! Let's solve the first half together.",
            6: "Let's walk through the reasoning steps together — you've got this!",
            7: "Wonderful perseverance! Here is the complete breakdown so you master it."
        }
        chosen_message = feedback_messages.get(level, "You're doing great — let's solve this together!")

        # 1. Level 1: Restate goal simply (in learner's interest domain)
        if level == 1:
            action = "hint" # legacy compatible
            next_representation = "standard"
            if hints:
                hint_text = hints[0]
            elif analogy_text:
                hint_text = f"Goal Restatement: {analogy_text}"
            else:
                hint_text = await ai_mentor_service.generate_gentle_hint(question, correct_answer, learner_context, 1)

            step_title = "Level 1: Goal Restatement"
            simplified_prompt = f"Goal: Find the option that completes '{question[:60]}...' safely."
            suggested_answer = "Focus on the main goal"
            eliminated_options = []
            guiding_question = None
            worked_example = None
            partial_step = None
            reasoning_walkthrough = None
            full_solution = None

        # 2. Level 2: Highlight Concept & Eliminate 1 Wrong Option
        elif level == 2:
            action = "change_representation" # legacy compatible
            next_representation = "visual_block" # legacy test_phase3 expects "visual_block"
            
            # Find an option to eliminate
            distractors = [opt for opt in options if str(opt).strip().lower() != correct_answer.strip().lower()]
            eliminated = distractors[0] if distractors else "Option D"
            eliminated_options = [eliminated]

            concept_name = concept_data.get("concept_name", "Core Concept")
            hint_text = f"Visual Clue: Imagine grouping into blocks! Notice '{concept_name}'. Also, '{eliminated}' is not correct."

            step_title = "Level 2: Concept Clue & Option Elimination"
            simplified_prompt = f"Distractor Eliminated: '{eliminated}' is ruled out. Focus on remaining choices."
            suggested_answer = f"Eliminated: {eliminated}"
            guiding_question = None
            worked_example = None
            partial_step = None
            reasoning_walkthrough = None
            full_solution = None

        # 3. Level 3: Guiding Socratic Question
        elif level == 3:
            action = "guiding_question"
            next_representation = "visual_block"
            
            if scaffold_steps:
                guiding_question = scaffold_steps[0]
            elif concept_data.get("learning_objectives"):
                guiding_question = f"Think about: {concept_data['learning_objectives'][0]}"
            else:
                guiding_question = f"What happens if we look at how '{correct_answer[:10]}...' relates to the question?"

            hint_text = f"Socratic Nudge: {guiding_question}"
            step_title = "Level 3: Guiding Socratic Question"
            simplified_prompt = guiding_question
            suggested_answer = "Reflect on this connection"
            eliminated_options = []
            worked_example = None
            partial_step = None
            reasoning_walkthrough = None
            full_solution = None

        # 4. Level 4: Small Worked Example with Analogous Numbers
        elif level == 4:
            action = "worked_example"
            next_representation = "simplified"

            if "×" in question or "*" in question or "multiply" in question.lower() or "calculate" in question.lower():
                worked_ex_prompt = "Parallel Example: Calculate 3 × 4"
                worked_ex_ans = "12 (3 groups of 4)"
            elif "nutrition" in question.lower() or "autotroph" in question.lower():
                worked_ex_prompt = "Parallel Example: An apple tree uses sunlight to make its food."
                worked_ex_ans = "The apple tree is an autotroph."
            elif "stomata" in question.lower() or "leaf" in question.lower():
                worked_ex_prompt = "Parallel Example: Fish have gills to breathe underwater."
                worked_ex_ans = "Leaves have microscopic pores (stomata) to exchange gases."
            else:
                worked_ex_prompt = "Parallel Example: Breaking a big problem into two simpler halves."
                worked_ex_ans = "Solve Part 1, then combine with Part 2."

            worked_example = {
                "scenario": worked_ex_prompt,
                "solution": worked_ex_ans
            }
            hint_text = f"Worked Example: {worked_ex_prompt} → Answer: {worked_ex_ans}."
            step_title = "Level 4: Small Worked Example"
            simplified_prompt = worked_ex_prompt
            suggested_answer = worked_ex_ans
            eliminated_options = []
            guiding_question = None
            partial_step = None
            reasoning_walkthrough = None
            full_solution = None

        # 5. Level 5: Partial Steps (Fill-in-the-blank)
        elif level == 5:
            action = "partial_steps"
            next_representation = "simplified"

            if scaffold_steps and len(scaffold_steps) > 1:
                fill_prompt = f"Step 1 is ready: {scaffold_steps[0]}. Now complete: {scaffold_steps[1]}"
            else:
                fill_prompt = f"Fill in the blank: The key feature matching our target is [ ______ ]."

            partial_step = {
                "prompt": fill_prompt,
                "clue": f"Relates closely to '{correct_answer}'"
            }
            hint_text = f"Partial Step: {fill_prompt}"
            step_title = "Level 5: Partial Steps"
            simplified_prompt = fill_prompt
            suggested_answer = "Fill in the missing step"
            eliminated_options = []
            guiding_question = None
            worked_example = None
            reasoning_walkthrough = None
            full_solution = None

        # 6. Level 6: Step-by-Step Reasoning Without Giving Away Final Answer
        elif level == 6:
            action = "explain_reasoning"
            next_representation = "simplified"

            walkthrough = []
            if scaffold_steps:
                walkthrough.extend(scaffold_steps)
            else:
                walkthrough.append("Step 1: Identify what is given in the problem statement.")
                walkthrough.append("Step 2: Connect the given terms to their scientific/mathematical definition.")
                if misconception_truth:
                    walkthrough.append(f"Key Fact: {misconception_truth}")
                walkthrough.append("Step 3: Select the option that aligns with this rule.")

            reasoning_walkthrough = walkthrough
            hint_text = f"Reasoning: {' '.join(walkthrough[:2])}"
            step_title = "Level 6: Step-by-Step Reasoning"
            simplified_prompt = "Review the step-by-step logic above to choose your answer."
            suggested_answer = "Apply this final step yourself"
            eliminated_options = []
            guiding_question = None
            worked_example = None
            partial_step = None
            full_solution = None

        # 7. Level 7: Full Solution Breakdown (Preserving Agency)
        else: # level >= 7
            action = "scaffold_and_reduce" # legacy compatible
            next_representation = "simplified" # legacy compatible

            sol_explanation = explanation or f"The correct answer is {correct_answer} because it directly satisfies the curriculum objective."
            hint_text = f"Simplified Example: If we take 1 group of {correct_answer}, the result is {correct_answer}!"

            full_solution = {
                "final_answer": correct_answer,
                "explanation": sol_explanation,
                "celebration": "You explored through all steps — learning takes curiosity and practice!"
            }
            step_title = "Level 7: Complete Worked Solution"
            simplified_prompt = f"Which of these matches {correct_answer}?" # legacy compatible
            suggested_answer = correct_answer # legacy compatible
            eliminated_options = []
            guiding_question = None
            worked_example = None
            partial_step = None
            reasoning_walkthrough = None

        scaffold_step = {
            "step_title": step_title,
            "simplified_prompt": simplified_prompt,
            "suggested_answer": suggested_answer
        }

        # Learner agency action choices
        agency_choices = ["Try independently now"]
        if level < 7:
            agency_choices.append(f"Request Level {level + 1} Hint")
        if next_representation != "visual_block":
            agency_choices.append("Switch to Visual Blocks")
        if next_representation != "simplified":
            agency_choices.append("Switch to Simplified Text")

        return {
            "feedback_message": chosen_message,
            "action": action,
            "next_representation": next_representation,
            "hint": hint_text,
            "scaffold_step": scaffold_step,
            "should_modify_strategy": attempt_count >= 2,
            # 7-Level Ladder Rich Metadata
            "scaffold_level": level,
            "level_name": step_title,
            "ladder_progress": {
                "current_level": level,
                "max_levels": 7,
                "can_advance": level < 7
            },
            "eliminated_options": eliminated_options,
            "guiding_question": guiding_question,
            "worked_example": worked_example,
            "partial_step": partial_step,
            "reasoning_walkthrough": reasoning_walkthrough,
            "full_solution": full_solution,
            "learner_agency_choices": agency_choices
        }

scaffold_engine = ScaffoldEngine()
