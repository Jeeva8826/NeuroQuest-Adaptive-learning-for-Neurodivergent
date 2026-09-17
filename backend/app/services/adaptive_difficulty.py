import logging
from typing import Dict, Any

logger = logging.getLogger("neuroquest.adaptive_difficulty")

class AdaptiveDifficultyPolicy:
    """
    First Adaptive Difficulty Engine.
    Uses rule-based heuristics over multi-signal behavioral inputs.
    Designed with a policy interface to allow future RL / Contextual Bandit policies to be plugged in.
    """

    def evaluate_next_difficulty(
        self,
        current_difficulty: int,
        accuracy_rate: float,
        avg_response_time_sec: float,
        hint_count: int,
        attempt_count: int,
        session_state: str = "FOCUSED",
        consecutive_correct: int = 0,
        consecutive_errors: int = 0
    ) -> Dict[str, Any]:
        """
        Determines difficulty adjustment: 'increase', 'maintain', 'decrease', 'scaffold', 'change_representation'.
        """
        target_difficulty = current_difficulty
        action = "maintain"
        reason = "Performance stable."

        # High engagement / high accuracy -> Increase difficulty
        if (accuracy_rate >= 0.85 or consecutive_correct >= 3) and session_state in ["FOCUSED", "HIGH_ENGAGEMENT"]:
            if current_difficulty < 5:
                target_difficulty = current_difficulty + 1
                action = "increase"
                reason = "High accuracy and focus detected. Challenge level increased."
            else:
                action = "maintain"
                reason = "Maximum difficulty reached."

        # Attention drift or fatigue -> Scaffold or Maintain with reduced cognitive load
        elif session_state in ["ATTENTION_DRIFT", "POSSIBLE_FATIGUE", "DISENGAGED"]:
            if current_difficulty > 1:
                target_difficulty = max(1, current_difficulty - 1)
                action = "decrease"
                reason = f"Learner state is '{session_state}'. Difficulty lowered for comfort."
            else:
                action = "change_representation"
                reason = f"Learner state is '{session_state}'. Switching to visual/audio representation."

        # Repeated errors or high response time -> Scaffold / Decrease
        elif consecutive_errors >= 2 or attempt_count >= 3 or avg_response_time_sec > 45.0 or hint_count >= 2:
            if current_difficulty > 1:
                target_difficulty = max(1, current_difficulty - 1)
                action = "decrease"
                reason = "Multiple attempts/hints needed. Simplifying task complexity."
            else:
                action = "scaffold"
                reason = "Minimum difficulty reached. Activating step scaffolding."

        return {
            "previous_difficulty": current_difficulty,
            "new_difficulty": target_difficulty,
            "action": action,
            "reason": reason,
            "policy_version": "1.0_heuristic_rule_engine" # Pluggable slot for contextual_bandit_v1
        }

adaptive_difficulty_engine = AdaptiveDifficultyPolicy()
