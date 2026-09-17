# NeuroQuest Privacy Policy

## 1. Core Principle
NeuroQuest is a learning tool, not a medical device. We adapt learning experiences based on observed interaction data, not clinical diagnoses.

## 2. What We Collect
We collect only what the learning loop needs:
- Answer correctness
- Attempt count
- Hint requests and revisits
- Time bands
- Explicit overload feedback ("Too much", "Too easy")
- Selected accessibility settings
- Modality choice
- Adaptation accepted/rejected

## 3. What We NEVER Collect
- ❌ Webcam feeds
- ❌ Facial recognition data
- ❌ Eye tracking
- ❌ EEG or biometric data
- ❌ Emotion recognition
- ❌ Continuous microphone recordings
- ❌ Raw keystroke surveillance
- ❌ Hidden behavioural monitoring
- ❌ Medical records
- ❌ Diagnosis probabilities

## 4. Data Storage
All interaction events are normalized through the `NormalizedAction` schema.
```json
{
  "raw_data_stored": false,
  "purpose": "learning_analytics"
}
```
No UI component directly changes the Bayesian Knowledge Tracing (BKT) engine without explicit, trackable events.

## 5. Compliance
Designed in alignment with the India DPDP Act provisions concerning children's data, including parental/guardian consent and restrictions around tracking/behavioural monitoring.
