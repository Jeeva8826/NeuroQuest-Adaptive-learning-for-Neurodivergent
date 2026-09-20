import os
import json
import logging
import re
from typing import Dict, Any, List, Optional
from app.services.rag_service import rag_service

logger = logging.getLogger("neuroquest.student_answer_evaluator")

class StudentAnswerEvaluator:
    """
    Structured Pedagogical Student Answer Evaluator for NeuroQuest.
    Provides gentle, non-punitive, neurodivergent-friendly evaluation of learner answers.
    Grounded in NCERT curriculum knowledge graph and diagnostic misconception catalogs.

    Output Schema:
    {
        "status": "CORRECT" | "INCORRECT" | "PARTIALLY_CORRECT" | "MISCONCEPTION_DETECTED",
        "reason": "Clear explanation of why this answer matches or diverges from the concept",
        "misconception": "Specific misconception identified or None",
        "correct_concept": "Core NCERT scientific or mathematical truth",
        "feedback": "Encouraging, strength-based feedback",
        "next_step": "Recommended next pedagogical action"
    }
    """

    def __init__(self):
        self._ncert_kg = None
        self._misconception_index = {}

    def _load_kg(self):
        if self._ncert_kg is not None:
            return
        base_dir = os.path.dirname(os.path.abspath(__file__))
        kg_path = os.path.normpath(os.path.join(base_dir, "..", "..", "..", "data", "curriculum", "ncert_knowledge_graph.json"))
        if os.path.exists(kg_path):
            try:
                with open(kg_path, "r", encoding="utf-8") as f:
                    self._ncert_kg = json.load(f)
                # Index misconceptions by concept_id and keyword
                for sub in self._ncert_kg.get("subjects", []):
                    for ch in sub.get("chapters", []):
                        for top in ch.get("topics", []):
                            for con in top.get("concepts", []):
                                cid = con.get("concept_id")
                                misconceptions = con.get("common_misconceptions", [])
                                if cid and misconceptions:
                                    self._misconception_index[cid] = misconceptions
            except Exception as e:
                logger.warning(f"Could not load NCERT Knowledge Graph for evaluator: {e}")

    def evaluate_answer(
        self,
        question: str,
        student_answer: str,
        correct_answer: str,
        options: Optional[List[str]] = None,
        concept_id: Optional[str] = None,
        task_context: Optional[Dict[str, Any]] = None,
        learner_context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        self._load_kg()
        task_context = task_context or {}
        learner_context = learner_context or {}

        s_ans_clean = str(student_answer).strip()
        c_ans_clean = str(correct_answer).strip()
        s_ans_lower = s_ans_clean.lower()
        c_ans_lower = c_ans_clean.lower()

        interests = learner_context.get("interests", ["space"])
        primary_interest = str(interests[0]).lower() if interests else "space"

        # Check for related concept in RAG if concept_id is missing
        concept_name = task_context.get("concept_name")
        explanation_text = task_context.get("explanation", "")
        misconceptions = []

        if concept_id and concept_id in self._misconception_index:
            misconceptions = self._misconception_index[concept_id]
        else:
            rag_hits = rag_service.search(f"{question} {correct_answer}", top_k=1)
            if rag_hits:
                hit = rag_hits[0]
                concept_id = concept_id or hit.get("concept_id")
                concept_name = concept_name or hit.get("concept_name")
                meta = hit.get("metadata", {})
                misconceptions = meta.get("common_misconceptions", [])
                if not explanation_text:
                    explanation_text = meta.get("simplified_explanation") or hit.get("content", "")

        scientific_truth = ""
        if misconceptions and isinstance(misconceptions[0], dict):
            scientific_truth = misconceptions[0].get("scientific_truth", "")

        correct_concept_str = (
            scientific_truth
            or explanation_text
            or f"The correct answer '{c_ans_clean}' directly satisfies the curriculum objective."
        )

        # -------------------------------------------------------------
        # 1. Exact Match -> CORRECT
        # -------------------------------------------------------------
        if s_ans_lower == c_ans_lower:
            return {
                "status": "CORRECT",
                "reason": f"Your response '{s_ans_clean}' is fully accurate and aligns with the NCERT curriculum benchmark.",
                "misconception": None,
                "correct_concept": correct_concept_str,
                "feedback": (
                    f"Outstanding thinking! Like an expert {primary_interest} explorer navigating new terrain, "
                    f"you grasped the concept accurately!"
                ),
                "next_step": "advance_to_next_challenge"
            }

        # -------------------------------------------------------------
        # 2. Check for Known Pedagogical Misconceptions
        # -------------------------------------------------------------
        detected_misconception = None
        for m in misconceptions:
            if isinstance(m, dict):
                m_text = m.get("misconception", "")
                m_words = [w for w in re.findall(r'\b\w+\b', m_text.lower()) if len(w) > 4]
                # Check if student's answer text or selected distractor matches misconception terms
                if s_ans_lower in m_text.lower() or any(w in s_ans_lower for w in m_words):
                    detected_misconception = m
                    break

        if detected_misconception:
            misc_desc = detected_misconception.get("misconception", "Common conceptual pitfall")
            truth_desc = detected_misconception.get("scientific_truth", correct_concept_str)
            return {
                "status": "MISCONCEPTION_DETECTED",
                "reason": (
                    f"You selected '{s_ans_clean}', which is a very common intuitive assumption. "
                    f"However, in scientific investigation: {truth_desc}"
                ),
                "misconception": misc_desc,
                "correct_concept": truth_desc,
                "feedback": (
                    f"You're in great company! Many curious minds explore this exact question. "
                    f"Let's look at what the evidence reveals: {truth_desc}"
                ),
                "next_step": "activate_scaffold_level_1"
            }

        # -------------------------------------------------------------
        # 3. Partial Match / Overlap -> PARTIALLY_CORRECT
        # -------------------------------------------------------------
        s_words = set(re.findall(r'\b\w+\b', s_ans_lower))
        c_words = set(re.findall(r'\b\w+\b', c_ans_lower))
        common = s_words & c_words

        if common and len(s_ans_clean) > 3 and len(c_ans_clean) > 3:
            return {
                "status": "PARTIALLY_CORRECT",
                "reason": (
                    f"You identified key aspects ({', '.join(common)}), but the full requirement "
                    f"calls for '{c_ans_clean}'."
                ),
                "misconception": "Incomplete conceptual specification",
                "correct_concept": correct_concept_str,
                "feedback": "You're on the right track! You spotted a core element. Let's complete the full picture.",
                "next_step": "refine_with_hint"
            }

        # -------------------------------------------------------------
        # 4. General Divergent Answer -> INCORRECT
        # -------------------------------------------------------------
        return {
            "status": "INCORRECT",
            "reason": (
                f"'{s_ans_clean}' does not match the expected answer '{c_ans_clean}'. "
                f"The question is exploring {concept_name or 'the core concept'}."
            ),
            "misconception": f"Divergence from standard definition of {concept_name or 'the concept'}",
            "correct_concept": correct_concept_str,
            "feedback": (
                "Great effort! Learning is an exploratory quest, and every attempt gives us new clues. "
                "Let's unlock a gentle hint to guide the way."
            ),
            "next_step": "activate_scaffold_level_0"
        }

student_answer_evaluator = StudentAnswerEvaluator()
