# NeuroQuest SIH Demo Script

This script walks through the **three most important demo moments** that demonstrate the platform's adaptive learning capabilities for neurodivergent learners.

## Moment 1: Before Adaptation (The Baseline)
1. **Setup**: The learner (Aarav, Class 7) logs into the platform. His Caregiver Support Profile is initialized but no specific adaptations have fired yet.
2. **Action**: Aarav navigates to the "Nutrition in Plants" lesson.
3. **Display**: The system shows the standard NCERT-aligned content:
   - A large block of text explaining photosynthesis.
   - A standard diagram.
   - A follow-up question with complex phrasing ("Explain the process...").
4. **Narrative**: "Here is what traditional platforms do. They present a large cognitive load and expect the student to parse it. Let's see what happens when the learner struggles."

## Moment 2: AI Detects Learning Mismatch
1. **Action**: Aarav answers the question incorrectly twice and takes longer than the expected time band.
2. **Trigger**: The system issues a "Load Check" directly to the learner: "How did that feel?"
3. **Action**: Aarav selects **"Too much"**.
4. **Narrative**: "Notice that we don't use webcams, EEG, or facial recognition to infer stress. We ask the learner directly. By combining BKT (Bayesian Knowledge Tracing - attempts/time) with explicit feedback ('Too much'), the Adaptation Engine fires with high confidence."

## Moment 3: The System Adapts
1. **Action**: The interface instantly transforms.
2. **Display**: 
   - The large text is replaced with a chunked, visual representation.
   - **"Let's learn ONE thing. How does a plant make food?"**
   - A simple icon flow: `Sunlight ☀️ -> Leaf 🍃 -> Food`
   - Scaffolding options appear: `[Try] [Hint] [Example]`
3. **Narrative**: "The AI didn't just give him the answer. It reduced the content density and increased the scaffold level. When Aarav now succeeds, his Mastery score goes from 42% -> 61%, the scaffold level automatically reduces for the next concept, and the UI explains: *'I reduced the amount of information because you indicated that the previous step felt overwhelming.'*"

## Conclusion (The Dashboard)
1. **Action**: Switch to the Educator/Caregiver dashboard.
2. **Display**: Shows that "Visual explanations" have an 87% success rate for Aarav. No diagnostic medical probabilities are shown—only actionable support profiles.
3. **Narrative**: "This is NeuroQuest. One learning objective. Multiple ways to reach it. Fully private, fully explainable."
