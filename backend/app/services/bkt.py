import numpy as np
import pandas as pd
from typing import Dict, Any, List

class BKTEngine:
    """
    Pandas & NumPy implementation of Bayesian Knowledge Tracing.
    Maps exactly to the Learner-State Estimation module from the Technical Approach Diagram.
    """
    def __init__(self):
        # Default BKT probabilities
        self.p_l0 = 0.5   # Initial probability of knowing
        self.p_t = 0.1    # Probability of learning
        self.p_s = 0.2    # Probability of slipping (knowing but answering wrong)
        self.p_g = 0.25   # Probability of guessing (not knowing but answering right)

    def calculate_new_mastery(self, current_mastery: float, correct: bool) -> float:
        """
        Updates the probability of mastery based on a single response.
        Utilizes NumPy scalar math for high-speed tensor compatibility later.
        """
        # Convert to numpy floats for precision
        p_mastery = np.float64(current_mastery)
        
        if correct:
            # P(L | correct)
            p_obs = (p_mastery * (1 - self.p_s)) / (
                p_mastery * (1 - self.p_s) + (1 - p_mastery) * self.p_g
            )
        else:
            # P(L | incorrect)
            p_obs = (p_mastery * self.p_s) / (
                p_mastery * self.p_s + (1 - p_mastery) * (1 - self.p_g)
            )
            
        # P(L_n+1) = P(L | obs) + (1 - P(L | obs)) * P(T)
        p_new = p_obs + (1 - p_obs) * self.p_t
        return float(p_new)

    def estimate_from_history(self, event_history: List[Dict[str, Any]]) -> float:
        """
        Pandas DataFrame calculation over a sequence of Learner interactions.
        """
        if not event_history:
            return self.p_l0
            
        df = pd.DataFrame(event_history)
        
        # Ensure 'correct' column exists and is boolean
        if 'correct' not in df.columns:
            return self.p_l0
            
        # Time-series mastery estimation
        mastery = self.p_l0
        for _, row in df.iterrows():
            mastery = self.calculate_new_mastery(mastery, bool(row['correct']))
            
        return mastery
