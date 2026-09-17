import os
import joblib
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from app.ml.synthetic_data import generate_synthetic_telemetry_dataset, FEATURE_COLUMNS, STATE_LABELS

logger = logging.getLogger("neuroquest.ml_train")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "learner_state_model.joblib")

def train_and_save_model():
    logger.info("Generating synthetic telemetry dataset for ML training...")
    df = generate_synthetic_telemetry_dataset(num_samples_per_class=400)
    
    X = df[FEATURE_COLUMNS]
    y = df["state_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    logger.info("Training Random Forest Classifier model...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
    clf.fit(X_train_scaled, y_train)

    y_pred = clf.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    logger.info(f"Model Training Complete. Accuracy: {acc * 100:.2f}%")

    model_data = {
        "model": clf,
        "scaler": scaler,
        "feature_columns": FEATURE_COLUMNS,
        "state_labels": STATE_LABELS,
        "accuracy": float(acc)
    }

    joblib.dump(model_data, MODEL_PATH)
    logger.info(f"Learner state ML model serialized to: {MODEL_PATH}")
    return model_data

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    train_and_save_model()
