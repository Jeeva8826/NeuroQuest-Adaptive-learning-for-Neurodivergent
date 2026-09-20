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
    Manages low-stress, non-punitive failure scaffolding with the 6-Level Architecture:
    
    - Level 0: Clarifying question (Orienting question to help understand what is being asked)
    - Level 1: Hint (Gentle hint or subtle clue without leaking the answer)
    - Level 2: Concept explanation (Core concept simplified with interest analogies & visual blocks)
    - Level 3: Example (Parallel worked example with analogous numbers/context)
    - Level 4: Step-by-step guidance (Structured reasoning & partial steps)
    - Level 5: Full explanation (Complete solution breakdown, celebration, & concept mastery)

    Connected directly with the contextual AI Assistant for safe, grounded learner guidance.
    """

    LEVEL_DEFINITIONS = {
        0: {"name": "Clarifying Question", "action": "clarifying_question", "representation": "standard"},
        1: {"name": "Hint", "action": "hint", "representation": "standard"},
        2: {"name": "Concept Explanation", "action": "change_representation", "representation": "visual_block"},
        3: {"name": "Example", "action": "worked_example", "representation": "simplified"},
        4: {"name": "Step-by-Step Guidance", "action": "partial_steps", "representation": "simplified"},
        5: {"name": "Full Explanation", "action": "scaffold_and_reduce", "representation": "simplified"}
    }

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
        question_text = str(task.get("question") or task.get("prompt", "")).lower()
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
        Generates a 6-level graduated scaffold step (Levels 0 to 5) grounded in NCERT.
        Preserves full backwards compatibility with tests and callers.
        """
        question = task.get("question") or task.get("prompt", "")
        correct_answer = str(task.get("correct_answer", ""))
        options = task.get("options", [])
        hints = task.get("hints", [])
        scaffold_steps = task.get("scaffold_steps", [])
        explanation = task.get("explanation", "")

        interests = learner_context.get("interests", ["space"])
        primary_interest = str(interests[0]).lower() if interests else "space"

        # Determine level in the 6-Level Architecture (0 to 5)
        output_scaffold_level = None
        if requested_level is not None:
            raw_lvl = int(requested_level)
            # Map legacy levels 6 and 7 gracefully to step guidance & full solution
            if raw_lvl >= 7:
                level = 5
                output_scaffold_level = raw_lvl
            elif raw_lvl == 6:
                level = 4
                output_scaffold_level = 6
            else:
                level = max(0, min(5, raw_lvl))
                output_scaffold_level = level
        else:
            if attempt_count <= 0:
                level = 0
            elif attempt_count == 1:
                level = 1
            elif attempt_count == 2:
                level = 2
            elif attempt_count == 3:
                level = 3
            elif attempt_count == 4:
                level = 4
            else:
                level = 5
            output_scaffold_level = level

        concept_data = self._find_concept_context(task)
        concept_name = concept_data.get("concept_name", "Core Concept")
        chapter_name = concept_data.get("chapter", "Curriculum Module")
        interest_analogies = concept_data.get("explanation", {}).get("interest_analogies", {})
        analogy_text = (
            interest_analogies.get(primary_interest)
            or interest_analogies.get("space")
            or concept_data.get("explanation", {}).get("simplified")
            or ""
        )
        misconceptions = concept_data.get("misconceptions", [])
        misconception_truth = misconceptions[0].get("scientific_truth") if misconceptions else ""

        # Non-punitive encouraging feedback messages for all 6 levels
        feedback_messages = {
            0: "Let's take a calm moment to clarify what the mission is asking!",
            1: "Good exploration! Here is a gentle hint to spark your thinking.",
            2: "Let's look at the big idea together with an engaging concept clue!",
            3: "Here is a quick parallel example to show how the pattern works!",
            4: "You're getting closer! Let's walk through the steps together.",
            5: "Wonderful perseverance! Here is the complete breakdown for concept mastery."
        }
        chosen_message = feedback_messages.get(level, "You're doing great — let's explore this together!")

        # Initialize slots
        clarifying_question = None
        hint_text = ""
        concept_explanation = None
        worked_example = None
        partial_step = None
        reasoning_walkthrough = None
        full_solution = None
        eliminated_options = []

        # ==============================================================
        # LEVEL 0: Clarifying Question
        # ==============================================================
        if level == 0:
            action = "clarifying_question"
            next_representation = "standard"
            step_title = "Level 0: Clarifying Question"

            if scaffold_steps:
                clarifying_question = f"Look at the question: {scaffold_steps[0]}"
            elif concept_data.get("learning_objectives"):
                clarifying_question = f"What is the main goal here? Are we looking for: {concept_data['learning_objectives'][0]}?"
            else:
                clarifying_question = f"What key property or relationship is '{question[:60]}...' asking us to notice?"

            hint_text = f"Orienting Question: {clarifying_question}"
            simplified_prompt = clarifying_question
            suggested_answer = "Identify what the question is asking"

        # ==============================================================
        # LEVEL 1: Hint
        # ==============================================================
        elif level == 1:
            action = "hint"
            next_representation = "standard"
            step_title = "Level 1: Hint"

            if hints:
                hint_text = hints[0]
            elif analogy_text:
                hint_text = f"Gentle Clue: {analogy_text}"
            else:
                hint_text = await ai_mentor_service.generate_gentle_hint(question, correct_answer, learner_context, 1)

            simplified_prompt = f"Goal: Find the option that connects to: '{hint_text[:60]}...'"
            suggested_answer = "Focus on the key clue"

        # ==============================================================
        # LEVEL 2: Concept Explanation (with Visual Block Mode & Distractor Cut)
        # ==============================================================
        elif level == 2:
            action = "change_representation"
            next_representation = "visual_block"
            step_title = "Level 2: Concept Explanation"

            distractors = [opt for opt in options if str(opt).strip().lower() != correct_answer.strip().lower()]
            eliminated = distractors[0] if distractors else "Option D"
            eliminated_options = [eliminated]

            concept_std = concept_data.get("explanation", {}).get("standard")
            concept_simp = concept_data.get("explanation", {}).get("simplified")
            concept_explanation = concept_simp or concept_std or f"The concept '{concept_name}' describes how elements interact in {chapter_name}."

            hint_text = f"Visual Clue: Imagine grouping into blocks! Notice '{concept_name}': {concept_explanation} Also, note '{eliminated}' is not correct."
            simplified_prompt = f"Distractor Eliminated: '{eliminated}' is ruled out. Concept focus: {concept_name}."
            suggested_answer = f"Eliminated: {eliminated}"

        # ==============================================================
        # LEVEL 3: Example (Parallel Worked Example)
        # ==============================================================
        elif level == 3:
            action = "worked_example"
            next_representation = "simplified"
            step_title = "Level 3: Example"

            if "×" in question or "*" in question or "multiply" in question.lower() or "calculate" in question.lower():
                scenario = "Parallel Example: Calculate 3 × 4"
                solution = "12 (3 equal groups of 4)"
            elif "nutrition" in question.lower() or "autotroph" in question.lower():
                scenario = "Parallel Example: A mango tree uses sunlight, water, and air to produce food."
                solution = "The mango tree is an autotroph because it makes its own food."
            elif "stomata" in question.lower() or "leaf" in question.lower() or "gas" in question.lower():
                scenario = "Parallel Example: Animals have nostrils to breathe air."
                solution = "Leaves have microscopic pores (stomata) through which carbon dioxide enters and oxygen exits."
            elif "fraction" in question.lower() or "ratio" in question.lower():
                scenario = "Parallel Example: Sharing 1 pizza equally among 4 friends."
                solution = "Each friend gets 1/4 of the whole pizza."
            else:
                scenario = f"Parallel Example: Testing a similar case with {concept_name}."
                solution = "Identify the defining feature, match with options."

            worked_example = {
                "scenario": scenario,
                "solution": solution,
                "takeaway": "Apply this identical pattern to solve the current question!"
            }
            hint_text = f"Worked Example: {scenario} → Takeaway: {solution}"
            simplified_prompt = scenario
            suggested_answer = solution

        # ==============================================================
        # LEVEL 4: Step-by-Step Guidance (Partial Steps & Structured Reasoning)
        # ==============================================================
        elif level == 4:
            action = "partial_steps"
            next_representation = "simplified"
            step_title = "Level 4: Step-by-Step Guidance"

            walkthrough = []
            if scaffold_steps and len(scaffold_steps) >= 2:
                walkthrough.extend(scaffold_steps)
                fill_prompt = f"Step 1: {scaffold_steps[0]}. Next step: [ ______ ]"
            else:
                walkthrough.append(f"Step 1: Identify what is given in the problem statement regarding '{concept_name}'.")
                walkthrough.append("Step 2: Connect the given terms to their scientific/mathematical definition.")
                if misconception_truth:
                    walkthrough.append(f"Key Principle: {misconception_truth}")
                walkthrough.append("Step 3: Select the option that directly satisfies this principle.")
                fill_prompt = f"Fill in the blank: The key feature matching '{concept_name}' is [ ______ ]."

            reasoning_walkthrough = walkthrough
            partial_step = {
                "prompt": fill_prompt,
                "clue": f"Relates closely to '{correct_answer[:4]}...'"
            }
            hint_text = f"Step Guidance: {' '.join(walkthrough[:2])}"
            simplified_prompt = fill_prompt
            suggested_answer = "Fill in the missing step"

        # ==============================================================
        # LEVEL 5: Full Explanation (Complete Worked Breakdown)
        # ==============================================================
        else: # level >= 5
            action = "scaffold_and_reduce"
            next_representation = "simplified"
            step_title = "Level 5: Full Explanation"

            sol_explanation = explanation or (
                f"The correct answer is '{correct_answer}'. In {chapter_name}, '{concept_name}' "
                f"is defined by this foundational principle."
            )
            hint_text = f"Full Solution: '{correct_answer}' is the correct choice because {sol_explanation}"

            full_solution = {
                "final_answer": correct_answer,
                "explanation": sol_explanation,
                "concept": concept_name,
                "celebration": "Incredible effort! You explored all 6 scaffold levels and mastered this curriculum concept!"
            }
            simplified_prompt = f"Which of these matches {correct_answer}?"
            suggested_answer = correct_answer

        if output_scaffold_level == 6:
            step_title = "Level 6: Step-by-Step Guidance"
        elif output_scaffold_level is not None and output_scaffold_level >= 7:
            step_title = f"Level {output_scaffold_level}: Full Explanation"

        scaffold_step = {
            "step_title": step_title,
            "simplified_prompt": simplified_prompt,
            "suggested_answer": suggested_answer
        }

        # Contextual AI Assistant connection payload
        contextual_assistant = {
            "scaffold_level": level,
            "level_name": step_title,
            "concept_id": concept_data.get("concept_id"),
            "concept_name": concept_name,
            "chapter": chapter_name,
            "suggested_prompt": (
                f"I'm on Scaffold Level {level} for '{concept_name}'. Can you explain how this connects to {primary_interest}?"
            ),
            "safety_policy": (
                "Never reveal the final answer before Level 5. Provide Socratic clues and conceptual analogies."
            ),
            "grounded_citation": f"NCERT {concept_data.get('standard', 'Curriculum')} - {chapter_name}"
        }

        # Learner agency action choices
        agency_choices = ["Try independently now"]
        if level < 5:
            agency_choices.append(f"Request Level {level + 1} ({self.LEVEL_DEFINITIONS[level + 1]['name']})")
        if next_representation != "visual_block":
            agency_choices.append("Switch to Visual Diagrams")
        if next_representation != "simplified":
            agency_choices.append("Switch to Simplified Text")

        return {
            "feedback_message": chosen_message,
            "action": action,
            "next_representation": next_representation,
            "hint": hint_text,
            "scaffold_step": scaffold_step,
            "should_modify_strategy": attempt_count >= 2,
            # 6-Level Architecture Fields
            "scaffold_level": output_scaffold_level,
            "architecture_level": level,
            "level_name": step_title,
            "ladder_progress": {
                "current_level": level,
                "max_levels": 6,
                "level_range": "Level 0 to Level 5",
                "can_advance": level < 5,
                "levels_roster": [
                    "Level 0: Clarifying question",
                    "Level 1: Hint",
                    "Level 2: Concept explanation",
                    "Level 3: Example",
                    "Level 4: Step-by-step guidance",
                    "Level 5: Full explanation"
                ]
            },
            "clarifying_question": clarifying_question,
            "concept_explanation": concept_explanation,
            "worked_example": worked_example,
            "example": worked_example,
            "partial_step": partial_step,
            "reasoning_walkthrough": reasoning_walkthrough,
            "step_by_step_guidance": reasoning_walkthrough or ([partial_step["prompt"]] if partial_step else None),
            "full_solution": full_solution,
            "full_explanation": full_solution,
            "eliminated_options": eliminated_options,
            "contextual_assistant": contextual_assistant,
            "learner_agency_choices": agency_choices
        }

scaffold_engine = ScaffoldEngine()
