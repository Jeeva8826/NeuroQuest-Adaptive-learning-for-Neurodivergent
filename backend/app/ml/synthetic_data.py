import os
import json
import logging
import numpy as np
import pandas as pd

logger = logging.getLogger("neuroquest.synthetic_data")

STATE_LABELS = {
    0: "FOCUSED",
    1: "ATTENTION_DRIFT",
    2: "POSSIBLE_FATIGUE",
    3: "DISENGAGED",
    4: "HIGH_ENGAGEMENT"
}

FEATURE_COLUMNS = [
    "gaze_drift_std",
    "gaze_offscreen_ratio",
    "click_rate_per_min",
    "rapid_click_count",
    "idle_ratio",
    "avg_response_time_sec",
    "incorrect_attempt_count",
    "hint_request_count",
    "session_duration_mins"
]

def load_empirical_benchmarks() -> dict:
    """Load pre-computed empirical WALS learner benchmarks if available."""
    try:
        benchmark_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "data", "processed", "personalization_benchmarks.json"
        ))
        if os.path.exists(benchmark_path):
            with open(benchmark_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        logger.debug(f"Could not load empirical benchmarks directly: {e}")
    return {}

def generate_synthetic_telemetry_dataset(num_samples_per_class: int = 300, random_seed: int = 42):
    """
    Generates a realistic synthetic training dataset for learner session telemetry state classification.
    Calibrated with empirical WALS neurodivergent learner statistics (N=10,000):
    - Session duration: mean 18.18 min, std 7.01 min, p25 13.3 min, p75 22.8 min
    - Task completion rate: ~69.2%
    - Fatigue onset: strongly correlated with prolonged sessions beyond p75 (>22.8 min)
    """
    np.random.seed(random_seed)
    benchmarks = load_empirical_benchmarks()
    
    # Grounded duration anchor from WALS benchmarks
    wals_mean_duration = benchmarks.get("session_duration_minutes", {}).get("mean", 18.18)
    wals_std_duration = benchmarks.get("session_duration_minutes", {}).get("std", 7.01)

    data = []
    
    for state_id in range(5):
        for _ in range(num_samples_per_class):
            if state_id == 0:  # FOCUSED
                gaze_drift = np.random.uniform(5.0, 25.0)
                offscreen = np.random.uniform(0.0, 0.1)
                click_rate = np.random.uniform(10.0, 30.0)
                rapid_clicks = np.random.poisson(0.2)
                idle_ratio = np.random.uniform(0.05, 0.2)
                response_time = np.random.uniform(4.0, 12.0)
                incorrects = np.random.poisson(0.3)
                hints = np.random.poisson(0.2)
                # Centered around typical productive duration (10-22 min)
                duration = float(np.clip(np.random.normal(wals_mean_duration * 0.85, 4.5), 2.0, 25.0))

            elif state_id == 1:  # ATTENTION_DRIFT
                gaze_drift = np.random.uniform(45.0, 120.0)
                offscreen = np.random.uniform(0.25, 0.6)
                click_rate = np.random.uniform(2.0, 12.0)
                rapid_clicks = np.random.poisson(0.5)
                idle_ratio = np.random.uniform(0.35, 0.7)
                response_time = np.random.uniform(15.0, 35.0)
                incorrects = np.random.poisson(1.2)
                hints = np.random.poisson(0.8)
                duration = float(np.clip(np.random.normal(wals_mean_duration, 5.5), 5.0, 30.0))

            elif state_id == 2:  # POSSIBLE_FATIGUE
                gaze_drift = np.random.uniform(30.0, 80.0)
                offscreen = np.random.uniform(0.15, 0.4)
                click_rate = np.random.uniform(4.0, 15.0)
                rapid_clicks = np.random.poisson(1.8) # increased clicking frustration
                idle_ratio = np.random.uniform(0.4, 0.75)
                response_time = np.random.uniform(20.0, 50.0) # sluggish response time
                incorrects = np.random.poisson(2.1)
                hints = np.random.poisson(1.5)
                # Fatigue rises as sessions exceed WALS p75 (22.8 mins)
                duration = float(np.clip(np.random.normal(28.0, 6.0), 22.0, 60.0))

            elif state_id == 3:  # DISENGAGED
                gaze_drift = np.random.uniform(70.0, 150.0)
                offscreen = np.random.uniform(0.5, 0.9)
                click_rate = np.random.uniform(0.0, 5.0)
                rapid_clicks = np.random.poisson(2.5)
                idle_ratio = np.random.uniform(0.7, 0.95)
                response_time = np.random.uniform(40.0, 90.0)
                incorrects = np.random.poisson(2.8)
                hints = np.random.poisson(2.0)
                duration = float(np.clip(np.random.normal(wals_mean_duration, wals_std_duration), 8.0, 45.0))

            elif state_id == 4:  # HIGH_ENGAGEMENT
                gaze_drift = np.random.uniform(2.0, 15.0)
                offscreen = np.random.uniform(0.0, 0.05)
                click_rate = np.random.uniform(25.0, 50.0)
                rapid_clicks = np.random.poisson(0.1)
                idle_ratio = np.random.uniform(0.0, 0.1)
                response_time = np.random.uniform(2.0, 6.0)
                incorrects = np.random.poisson(0.1)
                hints = np.random.poisson(0.05)
                duration = float(np.clip(np.random.normal(12.0, 3.5), 1.0, 20.0))

            row = [
                gaze_drift, offscreen, click_rate, float(rapid_clicks),
                idle_ratio, response_time, float(incorrects), float(hints),
                duration, state_id
            ]
            data.append(row)

    cols = FEATURE_COLUMNS + ["state_label"]
    df = pd.DataFrame(data, columns=cols)
    return df
