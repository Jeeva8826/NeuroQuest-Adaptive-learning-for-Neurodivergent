"""
Adaptation Engine for NeuroQuest.
Implements rule-based adaptations based on BKT and interaction history.
"""

from typing import Dict, Any, Optional

class AdaptationEngine:
    def __init__(self):
        pass

    def evaluate_adaptation(self, student_state: Dict[str, Any], interaction_history: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluates the student's current state and history to determine if an adaptation is needed.
        
        Args:
            student_state: dict containing 'mastery', 'cognitive_load_check' (e.g. "Too much", "Normal")
            interaction_history: dict containing 'attempts', 'recent_successes', 'learner_rejection'
            
        Returns:
            dict with 'adaptation_applied' (bool), 'adaptation_type' (str), 'explanation' (str), 'modifications' (dict)
        """
        mastery = student_state.get('mastery', 0.0)
        cognitive_load = student_state.get('cognitive_load_check', 'Normal')
        
        attempts = interaction_history.get('attempts', 0)
        recent_successes = interaction_history.get('recent_successes', 0)
        learner_rejection = interaction_history.get('learner_rejection', False)
        
        # Rule 4: Learner rejection (undo adaptation)
        if learner_rejection:
            return {
                "adaptation_applied": True,
                "adaptation_type": "Undo",
                "explanation": "You indicated the previous change wasn't helpful, so we've restored the original format.",
                "modifications": {
                    "difficulty": "reset",
                    "presentation": "default"
                }
            }

        # Rule 2: Explicit overload (load check = "Too much")
        if cognitive_load == "Too much":
            return {
                "adaptation_applied": True,
                "adaptation_type": "Reduce Load",
                "explanation": "You indicated you are feeling overwhelmed, so we're breaking the next steps into smaller, easier chunks.",
                "modifications": {
                    "presentation_style": "step-by-step",
                    "hide_extra_details": True,
                    "difficulty_adjustment": -1
                }
            }

        # Rule 1: Repeated difficulty (attempts >= 3 and mastery < 0.5)
        if attempts >= 3 and mastery < 0.5:
            return {
                "adaptation_applied": True,
                "adaptation_type": "Scaffolding",
                "explanation": "You've struggled with this a few times, so we've added extra hints and simplified the problem.",
                "modifications": {
                    "hints_enabled": True,
                    "difficulty_adjustment": -1
                }
            }

        # Rule 3: Mastery (mastery >= 0.75 + stable success)
        if mastery >= 0.75 and recent_successes >= 2:
            return {
                "adaptation_applied": True,
                "adaptation_type": "Challenge",
                "explanation": "You've been doing great, so we've slightly increased the challenge to keep things interesting!",
                "modifications": {
                    "difficulty_adjustment": 1,
                    "hints_enabled": False
                }
            }

        # No adaptation needed
        return {
            "adaptation_applied": False,
            "adaptation_type": "None",
            "explanation": "No changes made. Keep up the good work!",
            "modifications": {}
        }
