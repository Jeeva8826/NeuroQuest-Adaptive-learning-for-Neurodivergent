import os
import joblib
import logging
import numpy as np
import pandas as pd
from app.ml.train_model import MODEL_PATH, train_and_save_model
from app.ml.synthetic_data import FEATURE_COLUMNS, STATE_LABELS

logger = logging.getLogger("neuroquest.predict_service")

class LearnerStatePredictor:
    def __init__(self):
        self.model_data = None
        self.load_or_train()

    def load_or_train(self):
        if os.path.exists(MODEL_PATH):
            try:
                self.model_data = joblib.load(MODEL_PATH)
                logger.info(f"Loaded learner state ML model from {MODEL_PATH} (Accuracy: {self.model_data.get('accuracy', 0):.2f})")
            except Exception as e:
                logger.warning(f"Error loading model file: {e}. Retraining...")
                self.model_data = train_and_save_model()
        else:
            logger.info("Model file not found. Training new model...")
            self.model_data = train_and_save_model()

    def predict(self, telemetry: dict) -> dict:
        if not self.model_data:
            self.load_or_train()

        clf = self.model_data["model"]
        scaler = self.model_data["scaler"]

        # Non-camera fallback: if gaze data is missing or None, use default neutral values
        has_camera_gaze = telemetry.get("has_gaze", False)
        gaze_drift = telemetry.get("gaze_drift_std", 15.0 if has_camera_gaze else 20.0)
        offscreen = telemetry.get("gaze_offscreen_ratio", 0.05 if has_camera_gaze else 0.0)

        # Feature vector preparation
        feature_dict = {
            "gaze_drift_std": float(gaze_drift),
            "gaze_offscreen_ratio": float(offscreen),
            "click_rate_per_min": float(telemetry.get("click_rate_per_min", 15.0)),
            "rapid_click_count": float(telemetry.get("rapid_click_count", 0)),
            "idle_ratio": float(telemetry.get("idle_ratio", 0.1)),
            "avg_response_time_sec": float(telemetry.get("avg_response_time_sec", 8.0)),
            "incorrect_attempt_count": float(telemetry.get("incorrect_attempt_count", 0)),
            "hint_request_count": float(telemetry.get("hint_request_count", 0)),
            "session_duration_mins": float(telemetry.get("session_duration_mins", 5.0))
        }

        df_feat = pd.DataFrame([feature_dict])[FEATURE_COLUMNS]
        X_scaled = scaler.transform(df_feat)

        # Predict state & probabilities
        state_id = int(clf.predict(X_scaled)[0])
        probas = clf.predict_proba(X_scaled)[0]
        confidence = float(np.max(probas))

        state_name = STATE_LABELS.get(state_id, "FOCUSED")

        return {
            "state_id": state_id,
            "state_name": state_name,
            "confidence": round(confidence, 3),
            "has_camera_gaze": has_camera_gaze,
            "features_used": feature_dict
        }

predictor = LearnerStatePredictor()

def predict_learner_state(telemetry: dict) -> dict:
    return predictor.predict(telemetry)
