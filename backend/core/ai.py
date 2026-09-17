import json
import os
import google.generativeai as genai
from typing import Dict, Any

class AILearningEngine:
    """
    Core AI engine handling the RAG retrieval from NCERT curriculum
    and generating graduated scaffolding using Google Gemini.
    """
    
    def __init__(self):
        self.ncert_content_path = "data/curriculum/class7_science.json"
        
        # Configure Gemini (will safely fail over to mock if no API key is provided)
        api_key = os.getenv("GEMINI_API_KEY")
        model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        self.use_live_llm = bool(api_key)
        if self.use_live_llm:
            try:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel(model_name)
            except Exception:
                self.use_live_llm = False
        
    def retrieve_context(self, concept_id: str) -> str:
        """
        RAG retrieval. Fetches grounded, authorized NCERT curriculum data.
        """
        try:
            with open(self.ncert_content_path, "r") as f:
                data = json.load(f)
                # Find matching concept
                return data.get(concept_id, "Authorized NCERT context for this concept.")
        except FileNotFoundError:
            return f"NCERT curriculum context for: {concept_id}"

    def generate_scaffold(self, learner_state: Dict[str, Any], question: Dict[str, Any]) -> str:
        """
        Graduated scaffolding based on Bayesian Knowledge Tracing (BKT).
        If live LLM is enabled, asks Gemini to generate the specific scaffold step
        strictly grounded in the NCERT context.
        """
        mastery = learner_state.get("mastery", 0.0)
        attempts = learner_state.get("attempts", 0)
        base_context = self.retrieve_context(question.get("concept_id", ""))
        
        scaffold_level = self._determine_scaffold_level(mastery, attempts)
        
        if self.use_live_llm:
            try:
                prompt = (
                    f"You are a neuro-inclusive AI tutor.\n"
                    f"Context: {base_context}\n"
                    f"Question: {question.get('prompt')}\n"
                    f"Scaffold Level requested: {scaffold_level}\n"
                    f"Generate a strictly curriculum-aligned hint matching this exact scaffold level."
                )
                response = self.model.generate_content(prompt)
                if response and hasattr(response, "text") and response.text:
                    return response.text.strip()
            except Exception:
                pass

        # Fallback to deterministic mocks if no API key or on error
        if scaffold_level == "Restatement":
            return f"Let's re-read carefully: {question.get('prompt')}"
        elif scaffold_level == "Concept highlight":
            return f"Focus on this part of the concept: {base_context}"
        elif scaffold_level == "Clue":
            return f"Clue: Think about what happens when {question.get('concept_id')} occurs."
        elif scaffold_level == "Partial steps":
            return f"Let's break it down step-by-step: 1. {base_context}. 2. Now apply that here."
        else:
            return f"Example: Similar to how X works, {question.get('concept_id')} also uses energy."
                
    def _determine_scaffold_level(self, mastery: float, attempts: int) -> str:
        if mastery > 0.7: return "Restatement"
        elif mastery > 0.5: return "Concept highlight"
        elif mastery > 0.3: return "Clue"
        elif attempts > 2: return "Partial steps"
        else: return "Example"

    def adapt_content(self, learner_profile: Dict[str, Any], content: str) -> str:
        if learner_profile.get("visual_preference") == "High":
            return f"[VISUAL DIAGRAM PLACEHOLDER]\n{content}"
        if learner_profile.get("chunking_preference") == "High":
            chunks = content.split(". ")
            return "\n\n".join([f"Step {i+1}: {chunk}." for i, chunk in enumerate(chunks) if chunk])
        return content
