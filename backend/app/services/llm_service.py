import logging
import httpx
from app.config import settings

logger = logging.getLogger("neuroquest.llm_service")

async def generate_adaptive_explanation(
    question: str,
    correct_answer: str,
    learner_interests: list = None,
    guidance_level: str = "high"
) -> str:
    """
    Generates a gentle, neurodivergent-friendly simplified explanation or hint
    tailored to the learner's interests (e.g. Space, Animals, Coding).
    Tries Ollama first, falls back to Groq API, then uses structured fallback.
    """
    interest_context = ", ".join(learner_interests) if learner_interests else "Space and Exploration"
    
    prompt = (
        f"You are a warm, encouraging AI guide for a neurodivergent learner who loves {interest_context}.\n"
        f"Task Question: {question}\n"
        f"Correct Answer: {correct_answer}\n"
        f"Provide a clear, simple, low-stress 2-sentence explanation or hint in a encouraging tone using metaphors from {interest_context}."
    )
    
    # 1. Try Ollama (Local)
    if settings.OLLAMA_BASE_URL:
        try:
            async with httpx.AsyncClient(timeout=3.0) as client:
                resp = await client.post(
                    f"{settings.OLLAMA_BASE_URL}/api/generate",
                    json={
                        "model": settings.OLLAMA_MODEL,
                        "prompt": prompt,
                        "stream": False
                    }
                )
                if resp.status_code == 200:
                    data = resp.json()
                    response_text = data.get("response", "").strip()
                    if response_text:
                        return response_text
        except Exception as e:
            logger.debug(f"Ollama local LLM unavailable: {e}")

    # 2. Try Groq API (Fallback)
    if settings.GROQ_API_KEY:
        try:
            async with httpx.AsyncClient(timeout=4.0) as client:
                headers = {"Authorization": f"Bearer {settings.GROQ_API_KEY}"}
                payload = {
                    "model": "llama3-8b-8192",
                    "messages": [
                        {"role": "system", "content": "You are a gentle, supportive tutor for neurodivergent learners."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": 150
                }
                resp = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    content = data["choices"][0]["message"]["content"].strip()
                    if content:
                        return content
        except Exception as e:
            logger.debug(f"Groq API unavailable: {e}")

    # 3. Try Gemini API (Fallback)
    if settings.GEMINI_API_KEY:
        try:
            import google.generativeai as genai
            genai.configure(api_key=settings.GEMINI_API_KEY)
            model = genai.GenerativeModel(settings.GEMINI_MODEL)
            resp = await model.generate_content_async(prompt)
            if resp and hasattr(resp, "text") and resp.text:
                return resp.text.strip()
        except Exception as e:
            logger.debug(f"Gemini API unavailable: {e}")

    # 4. Rule-based adaptive fallback
    return (
        f"Great effort! Remember that '{correct_answer}' is the right fit here. "
        f"Just like exploring in {interest_context}, taking it step by step makes learning easy and fun!"
    )
