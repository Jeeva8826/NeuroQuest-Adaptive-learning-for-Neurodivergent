import logging
import json
import httpx
from typing import Dict, Any, List, Optional
from app.config import settings

logger = logging.getLogger("neuroquest.ai_mentor")

class AIMentorProvider:
    """Abstract Base Class for AI Mentor LLM Providers."""
    async def generate_response(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        raise NotImplementedError

class OllamaMentorProvider(AIMentorProvider):
    """Primary LLM Provider using local Ollama instance."""
    def __init__(self, base_url: str = None, model: str = None):
        self.base_url = base_url or settings.OLLAMA_BASE_URL
        self.model = model or settings.OLLAMA_MODEL

    async def generate_response(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        if not self.base_url:
            return None
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        try:
            async with httpx.AsyncClient(timeout=4.0) as client:
                resp = await client.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": full_prompt,
                        "stream": False
                    }
                )
                if resp.status_code == 200:
                    text = resp.json().get("response", "").strip()
                    if text:
                        return text
        except Exception as e:
            logger.debug(f"Ollama provider failed: {e}")
        return None

class GroqMentorProvider(AIMentorProvider):
    """Fallback LLM Provider using Groq API."""
    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.GROQ_API_KEY

    async def generate_response(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        if not self.api_key:
            return None
        try:
            async with httpx.AsyncClient(timeout=4.0) as client:
                headers = {"Authorization": f"Bearer {self.api_key}"}
                payload = {
                    "model": "llama3-8b-8192",
                    "messages": [
                        {"role": "system", "content": system_prompt or "You are an encouraging AI Mentor for neurodivergent learners."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": 300
                }
                resp = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
                if resp.status_code == 200:
                    text = resp.json()["choices"][0]["message"]["content"].strip()
                    if text:
                        return text
        except Exception as e:
            logger.debug(f"Groq API provider failed: {e}")
        return None

class GeminiMentorProvider(AIMentorProvider):
    """Cloud LLM Provider using Google Gemini."""
    def __init__(self, api_key: str = None, model: str = None):
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.model_name = model or settings.GEMINI_MODEL
        self._model = None
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self._model = genai.GenerativeModel(self.model_name)
            except Exception as e:
                logger.debug(f"Gemini mentor provider init failed: {e}")

    async def generate_response(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        if not self.api_key or not self._model:
            return None
        try:
            full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
            response = await self._model.generate_content_async(full_prompt)
            if response and hasattr(response, "text") and response.text:
                return response.text.strip()
        except Exception as e:
            logger.debug(f"Gemini API provider failed: {e}")
        return None

class RuleBasedMentorProvider(AIMentorProvider):
    """Safety Fallback Provider using deterministic rule templates."""
    async def generate_response(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        return None

class AIMentor:
    """Orchestrates Groq, Gemini, Ollama, and rule-based AI Mentor operations."""

    def __init__(self):
        self.providers: List[AIMentorProvider] = [
            GroqMentorProvider(),
            GeminiMentorProvider(),
            OllamaMentorProvider(),
            RuleBasedMentorProvider()
        ]

    async def _query_llm(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        for provider in self.providers:
            res = await provider.generate_response(prompt, system_prompt)
            if res:
                return res
        return None

    async def generate_personalized_mission_task(
        self,
        subject: str,
        learner_context: Dict[str, Any],
        base_objective: str = "Solve basic arithmetic challenges",
        difficulty: int = 1
    ) -> Dict[str, Any]:
        """
        Wraps generic educational objectives into a theme-aware personalized mission task.
        """
        interests = learner_context.get("interests", ["space"])
        primary_interest = interests[0] if interests else "Space"
        state = learner_context.get("currentState", "FOCUSED")
        learning_mode = learner_context.get("preferredLearningMode", "visual")

        sys_prompt = (
            "You are NeuroQuest AI Mentor, creating tailored educational missions for neurodivergent learners. "
            "Never assume what motivates a learner. Deliver low-stress, highly engaging narrative missions."
        )

        user_prompt = (
            f"Subject: {subject}\n"
            f"Learner Primary Interest: {primary_interest}\n"
            f"Current Learner State: {state}\n"
            f"Preferred Learning Mode: {learning_mode}\n"
            f"Difficulty Level: {difficulty}\n"
            f"Educational Objective: {base_objective}\n"
            f"Construct a personalized mission in JSON format with fields: title, mission_narrative, question, options (4 items), correct_answer, explanation, hint."
        )

        raw_llm = await self._query_llm(user_prompt, sys_prompt)
        if raw_llm:
            try:
                # Extract JSON from code block if present
                clean_json = raw_llm.strip()
                if "```json" in clean_json:
                    clean_json = clean_json.split("```json")[1].split("```")[0].strip()
                elif "```" in clean_json:
                    clean_json = clean_json.split("```")[1].split("```")[0].strip()
                parsed = json.loads(clean_json)
                return parsed
            except Exception as e:
                logger.debug(f"Could not parse LLM JSON task: {e}")

        # Rule-based structured fallback
        return self._generate_rule_fallback_task(subject, primary_interest, base_objective, difficulty)

    def _generate_rule_fallback_task(self, subject: str, interest: str, objective: str, difficulty: int) -> Dict[str, Any]:
        interest_lower = interest.lower()
        if "space" in interest_lower or "star" in interest_lower or "rocket" in interest_lower:
            return {
                "title": f"Mission: Repair the {subject} Satellite",
                "mission_narrative": f"The station power grid needs your mathematical calculations! Help align the solar panels for {subject}.",
                "question": f"To power up the {subject} satellite relay, calculate: 4 × {difficulty + 2}",
                "options": [str(4 * (difficulty + 2)), str(4 * (difficulty + 2) + 2), str(4 * (difficulty + 2) - 3), str(4 * (difficulty + 2) + 5)],
                "correct_answer": str(4 * (difficulty + 2)),
                "explanation": f"Great job commander! 4 × {difficulty + 2} gives {4 * (difficulty + 2)} power units to the satellite.",
                "hint": f"Try counting in groups of 4 or breaking {difficulty + 2} into smaller steps!"
            }
        elif "animal" in interest_lower or "pet" in interest_lower or "nature" in interest_lower:
            return {
                "title": f"Mission: Wildlife Sanctuary {subject} Care",
                "mission_narrative": f"The rescue sanctuary needs food allocation measurements for our newly arrived animals!",
                "question": f"Each habitat gets 5 feeding bowls. How many total bowls are needed for {difficulty + 1} habitats?",
                "options": [str(5 * (difficulty + 1)), str(5 * (difficulty + 1) + 3), str(5 * (difficulty + 1) - 2), "10"],
                "correct_answer": str(5 * (difficulty + 1)),
                "explanation": f"Wonderful rescue work! {difficulty + 1} habitats × 5 bowls = {5 * (difficulty + 1)} total bowls.",
                "hint": "Count by 5s for each habitat!"
            }
        else:
            return {
                "title": f"Mission: Custom {interest.capitalize()} Exploration",
                "mission_narrative": f"Welcome to your custom {interest} challenge! Solve this step to advance your quest.",
                "question": f"Select the correct answer to complete this {subject} milestone step.",
                "options": ["Option A (Correct)", "Option B", "Option C", "Option D"],
                "correct_answer": "Option A (Correct)",
                "explanation": f"Excellent work on your {interest} exploration journey!",
                "hint": "Take your time and look for pattern clues."
            }

    async def generate_gentle_hint(
        self,
        question: str,
        correct_answer: str,
        learner_context: Dict[str, Any],
        attempt_count: int = 1
    ) -> str:
        """Generates a low-stress hint tailored to learner interests and current state."""
        interests = learner_context.get("interests", ["space"])
        primary_interest = interests[0] if interests else "Exploration"
        
        prompt = (
            f"The learner is attempting: {question}\n"
            f"Correct Answer: {correct_answer}\n"
            f"Learner Interest: {primary_interest}\n"
            f"Attempt Count: {attempt_count}\n"
            f"Provide a friendly, gentle hint (1-2 sentences) using a metaphor from {primary_interest}. "
            f"Do not say 'Wrong' or 'Incorrect'."
        )

        res = await self._query_llm(prompt, "You are a gentle AI mentor.")
        if res:
            return res

        return f"Let's look at this another way! In your {primary_interest} journey, taking it one step at a time helps us find '{correct_answer}' easily."

    async def generate_daily_welcome_mission(
        self,
        learner_name: str,
        learner_context: Dict[str, Any],
        recent_performance: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generates a personalized daily return experience instead of generic streaks."""
        interests = learner_context.get("interests", ["Space"])
        primary_interest = interests[0] if interests else "Space"
        
        prompt = (
            f"Learner Name: {learner_name}\n"
            f"Primary Interest: {primary_interest}\n"
            f"Recent Performance: {recent_performance}\n"
            f"Construct a welcoming daily mission introduction (2 sentences) and mission goal title. "
            f"Example: 'Welcome back, Explorer Leo! Your last space mission was successful. Today you're going to repair the Moon Base.'"
        )

        res = await self._query_llm(prompt, "You are a warm, encouraging educational mentor.")
        if res:
            return {
                "greeting": res,
                "mission_title": f"Today's Personalized {primary_interest} Mission",
                "theme": primary_interest.lower()
            }

        return {
            "greeting": f"Welcome back, Commander {learner_name}! 🚀 Your previous quest went smoothly. Today, let's explore a new {primary_interest} frontier together!",
            "mission_title": f"Today's Personalized {primary_interest} Mission",
            "theme": primary_interest.lower()
        }

ai_mentor_service = AIMentor()
