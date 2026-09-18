# NeuroQuest: Dataset-to-Questionnaire Educational Traceability Matrix

## 1. Executive Overview & Methodology

The NeuroQuest caregiver onboarding questionnaire constructs the learner's **Initial Learning Support Profile**. Rather than displaying raw clinical screening instruments or generic questionnaire columns, NeuroQuest implements a strict **Educational Translation Pipeline**:

```
DATASET / RESEARCH VARIABLE
          ↓
EDUCATIONAL RELEVANCE ANALYSIS
          ↓
SAFE CAREGIVER QUESTION (Non-Diagnostic)
          ↓
LEARNING-SUPPORT FEATURE
          ↓
INITIAL LEARNER PROFILE (Baseline)
          ↓
REAL INTERACTION TELEMETRY
          ↓
DYNAMIC ADAPTATION ENGINE
```

---

## 2. Dataset Usability Audit & Classification

| Dataset / Instrument | Source / Origin | Usability Category | Usability Verdict | Educational Translation & Extraction | Excluded Elements |
|---|---|---|---|---|---|
| **NCERT Curriculum & Knowledge Graph** | NCERT Class 6–8 Books (`adityasharma01/ncert-books`) | **Category A** (Pedagogical Content) | **100% USABLE** | Direct mapping to curriculum tasks, grade bands, subject hierarchies (Science, Math, Social Science), difficulty calibration (1.0–3.0), and topic taxonomy. | None |
| **Learning Analytics & Representation Benchmarks** | Assistments / EdNet / UCI Student Performance | **Category A** (Pedagogical Content) | **100% USABLE** | Extracted variables for representation modality preference (visual vs. text vs. worked example), task size chunking, and feedback delivery preference. | Raw user IDs, institutional grades |
| **Cognitive Load & Behavioral Telemetry** | Cognitive research / `synthetic_data.py` | **Category B** (Behavioral Indicators) | **100% USABLE (Translated)** | Translated telemetry variables (`click_rate`, `idle_ratio`, `rapid_click`, `gaze_drift`) into observable home/school learning behaviors (task initiation friction, struggle response, break needs). | Raw diagnostic inferences |
| **ICMR Pediatric Assessment Proxy** | INCLEN Pediatric Neurodevelopmental Research (`shibumohapatra/icmr-data`, `n1sarg/icmr-testing-data`) | **Category C** (Medical / Screening Data) | **PARTIALLY USABLE (Strictly Non-Diagnostic)** | **Safely Extracted**: Environmental sensitivities (sound, motion), pace preferences, existing formal support categories (`caregiver_reported_support_information`). | **PURGED**: Seizure history (ICMR-15), EEG findings, Family history (ICMR-20), Clinical cutoff scores, DSM/ICD diagnostic calculators. |
| **ASD / ADHD Screening Instruments** | AQ-10 Child, Q-CHAT, ASSQ, Vanderbilt Rating Scale (`fabdelja/asd-screening-data`, `raiyangani/autistic-spectrum-disorder-screening-data`) | **Category C** (Medical / Screening Data) | **PARTIALLY USABLE (Strictly Non-Diagnostic)** | **Safely Extracted**: Predictable routine preferences, clear transition warnings, sensory overwhelm mitigation (calm mode, visual density). | **PURGED**: Clinical threshold scores, screening diagnoses, diagnostic prediction classifiers. |

---

## 3. Comprehensive 10-Step Question Traceability Matrix (28 Questions)

### Step 1: Learner & Education (Category A — NCERT & Educational Foundation)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q1.1** | `learner_name_grade` | NCERT Class 6–8 Curriculum Hierarchy | Personalization establishes rapport and age-appropriate vocabulary level. | *"What is your learner's preferred name and current grade level?"* | `learner_name`, `grade_level` | Initializes baseline vocabulary difficulty and NCERT topic progression. |
| **Q1.2** | `primary_subjects` | NCERT Subject Standards (`adityasharma01/ncert-books`) | Identifies primary focus domains where the learner will spend study time. | *"Which subjects are the primary focus for learning support?"* | `primary_subjects` | Directs task generator to prioritized subject modules (Science, Math, Logic). |
| **Q1.3** | `interest_anchors` | Learner Engagement Research (EdNet / Assistments) | Deep special interests dramatically increase dopamine-driven task persistence in neurodivergent learners. | *"What are the learner's high-interest passion topics? (e.g., Space, Animals, Coding, Mythology)"* | `interests`, `theme_anchor` | Anchors AI mentor analogies, mission themes, background visuals, and unlockable rewards. |

---

### Step 2: Known Support Information — Optional (Category C — Disclaimed Accommodations)

> [!NOTE]
> This section is strictly optional and disclaimed. It never computes or assigns diagnostic labels.

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q2.1** | `has_formal_support` | ICMR-1–4 / IEP Educational Support Flags | Knowing whether formal accommodations already exist prevents frustrating trial-and-error in classroom adaptations. | *"Has the learner been identified by a school or specialist as having an educational learning or support need?"* (Yes / No / Unsure / Prefer not to say) | `has_identified_support` | Conditionally displays Q2.2 if 'Yes'; otherwise skips smoothly to Step 3. |
| **Q2.2** | `support_categories` | ICMR / INCLEN Support Framework Categories | Categorizing functional support requirements allows pre-activation of proven educational accommodations. | *(Conditional)* *"Which general areas of educational support are relevant? (Attention, Reading, Writing, Math, Communication, Sensory)"* | `caregiver_reported_support_information` | Pre-tunes baseline scaffolding ladder and sensory density filters without clinical labels. |

---

### Step 3: Learning Strengths & Representation (Category A — Pedagogical Representation)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q3.1** | `representation_mode` | Assistments Modality Study (Visual vs. Text vs. Worked Example) | Learners process concepts faster when presented in their preferred cognitive modality. | *"What type of material usually helps the learner understand a new topic best?"* | `learning_representation` | Selects default task presentation: interactive diagram, video brief, or worked-example card. |
| **Q3.2** | `engagement_anchors` | Assistments Activity Logs (Game vs. Practice vs. Explorer) | Intrinsic motivation styles differ widely; exploration quests vs. logic challenges yield higher completion rates. | *"Which learning activities consistently keep the learner engaged and curious?"* | `engagement_preferences` | Sets default activity structure in daily return missions (`/api/ai/daily-welcome`). |
| **Q3.3** | `interest_boost` | EdNet Engagement Multipliers | Quantifies the effectiveness of integrating special interests into practice questions. | *"How much does connecting lessons to their special interest improve focus and enthusiasm?"* | `interest_integration_weight` | Tunes the ratio of interest-grounded analogies used in Socratic explanations (`/api/ai/explain`). |

---

### Step 4: Learning Difficulties & Processing (Category A & B)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q4.1** | `reading_text_volume` | Dyslexia / Cognitive Load Reading Limits | Excessive continuous text triggers cognitive fatigue and avoidant abandonment. | *"What amount of continuous reading text is most comfortable per screen?"* | `text_tolerance`, `visual_density` | Chunks reading cards into 1–2 line bites, short paragraphs, or icon-assisted bullet points. |
| **Q4.2** | `academic_triggers` | Assistments Error Distribution Logs | Identifies cognitive roadblocks (e.g., multi-step word problems or dense definitions). | *"Which academic tasks usually trigger struggle, anxiety, or avoidance?"* | `observed_learning_difficulties` | Auto-activates Socratic step-by-step breakdowns for flagged concept formats. |
| **Q4.3** | `difficulty_response` | Cognitive Scaffolding Research | Identifies the most effective remediation vector when unfamiliar material is introduced. | *"When a new topic is difficult, what usually helps most to bridge understanding?"* | `scaffolding_preference` | Prioritizes either parallel worked examples, vocabulary hints, or visual diagrams in `/api/ai/scaffold`. |

---

### Step 5: Attention & Task Management (Category B — Executive Function Indicators)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q5.1** | `task_management_friction`| Vanderbilt / ICMR Inattention Behavioral Scale (Translated) | Executive function hurdles (task initiation, organization, multi-step memory) require structural UI supports. | *"Which parts of independent learning are usually difficult? (Starting, organizing, remembering steps, switching tasks)"* | `task_management_support` | Renders visual step checklists, countdown warmups, and singular action cards. |
| **Q5.2** | `frustration_behavior` | Cognitive Load Behavioral States (`synthetic_data.py`) | Informs the platform how to react gracefully when error thresholds are crossed. | *"What usually happens when a task becomes frustrating or difficult?"* | `frustration_recovery_strategy` | When repeated errors occur, triggers a gentle sensory breather rather than escalating challenge. |
| **Q5.3** | `session_fatigue_pattern` | Interaction Duration Benchmarks (EdNet Session Lengths) | Cognitive stamina varies; rigid session durations cause attention drift. | *"How does the learner usually respond to longer learning sessions?"* | `session_length_preference` | Sets optimal session cap (e.g. 5–7 mins micro-bursts vs. 15 mins) and schedules periodic check-ins. |

---

### Step 6: Accessibility & Sensory Preferences (Category B & C — Sensory Regulation)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q6.1** | `visual_accessibility` | W3C WCAG 2.1 & Neurodiversity Guidelines | Sensory overload from motion, low contrast, or complex typography degrades processing speed. | *"Which visual accessibility supports are helpful? (Dyslexic font, larger text, reduced motion, high contrast)"* | `accessibility_preferences` | Injects OpenDyslexic font, disables parallax/animations, and enables high-contrast themes. |
| **Q6.2** | `audio_preferences` | Assistments TTS & Audio Clutter Studies | Unsolicited sounds can startle or distract auditory-sensitive learners. | *"How should sound and audio read-aloud be configured?"* | `sensory_preferences.audio` | Configures audio reader to on-demand button vs. automatic narration, or mutes ambient chimes. |
| **Q6.3** | `color_palette` | Sensory Calming Color Psychology | Calming muted pastels vs. high-contrast modes reduce visual stress. | *"Which color palette style feels most comfortable to look at?"* | `visual_preferences.palette` | Activates soft pastel, high contrast dark, or minimalist theme palettes globally. |

---

### Step 7: Communication & Instruction Preferences (Category A — Instructional Design)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q7.1** | `instruction_granularity`| Universal Design for Learning (UDL Principle 1) | Multi-clause sentences cause working memory overload. | *"How does the learner prefer instructions to be delivered?"* | `instruction_style` | AI mentor limits instructions to single-clause bullet points with one actionable click. |
| **Q7.2** | `feedback_style` | Assistments Immediate Feedback vs. Delayed Socratic | Punitive feedback creates anxiety; constructive guidance builds growth mindset. | *"When the learner makes a mistake, what feedback style helps most?"* | `feedback_style` | Suppresses red error banners; serves gentle scaffolded hints and partial-credit encouragement. |
| **Q7.3** | `pacing_control` | Cognitive Processing Latency Benchmarks | Timed clocks trigger executive freeze in anxiety-prone learners. | *"What pacing rhythm works best during tasks?"* | `pacing_preference` | Completely removes timers from quiz screens; allows unlimited dwell time. |

---

### Step 8: Existing Educational Accommodations (Category C — Established School Supports)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q8.1** | `accommodations_used` | IEP / 504 Plan Standard Classroom Accommodations | Bridges home/school accommodations into the digital learning interface. | *"Does the learner currently use any educational accommodations in school or at home?"* | `existing_accommodations` | Activates digital equivalents (extra time, audio reader, reduced visual clutter, step checklists). |
| **Q8.2** | `effective_accommodations`| Educational Support Review Logs | Prioritizes the highest-impact accommodations that have historically worked best. | *(Conditional)* *"Which of these accommodations have proven most effective in practice?"* | `priority_accommodations` | Weights matching adaptation features with highest priority in the adaptation engine. |

---

### Step 9: Learning Environment & Motivation (Category B — Motivation Architecture)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q9.1** | `study_environment` | Sensory Environmental Audits | External background noise level impacts internal cognitive reserve. | *"Where and in what type of environment does the learner study best?"* | `environment_preferences` | Suggests matching audio-visual themes (e.g. quiet ambient nature sounds vs. silent space). |
| **Q9.2** | `break_rhythm` | Telemetry Cognitive Fatigue Thresholds | Proactive breaks prevent meltdown and cognitive exhaustion before they occur. | *"How often should the platform suggest a gentle sensory break or breather?"* | `sensory_break_interval` | Configures the telemetry engine to prompt calm breathing visual pauses every 5–7 mins. |
| **Q9.3** | `celebration_style` | Non-Competitive Gamification Research | Loud flashing animations or competitive scoreboards cause stress or sensory overstimulation. | *"What type of achievement acknowledgment is preferred?"* | `motivation_preferences` | Replaces noisy celebratory fanfare with quiet star collections, area unlocks, or badge vaults. |

---

### Step 10: Consent, Review & Profile Generation (Privacy & Verification)

| Q# | Question Identifier | Source Dataset / Variable | Educational Relevance Analysis | Safe Non-Diagnostic Question Text | Target Profile Field | Dynamic Adaptation Trigger |
|:---:|---|---|---|---|---|---|
| **Q10.1** | `review_and_consent` | COPPA, FERPA & Ethics in Educational AI | Explicit caregiver transparency and informed consent ensure privacy compliance. | *"I confirm this information is provided voluntarily to personalize educational delivery and understand NeuroQuest does not diagnose medical conditions."* | `consent` | Compiles the 14-dimension `InitialLearnerSupportProfile` and unlocks the learner's personalized game world. |

---

## 4. Structured Initial Learner Support Profile Output

When Step 10 is submitted, the backend translates the 28 responses into the unified **14-Dimension Initial Learning Support Profile**:

```json
{
  "learner_id": "learner_67890",
  "caregiver_id": "user_12345",
  "learner_name": "Leo",
  "grade_level": "Class 6",
  "learning_representation": ["visual_diagrams", "worked_examples"],
  "instruction_style": ["single_step", "concrete_example_first"],
  "task_size_preference": "small",
  "session_length_preference": "short_micro_sessions",
  "feedback_style": ["gentle_hint_first", "explain_gently"],
  "scaffolding_preference": ["parallel_worked_example", "eliminate_distractors"],
  "engagement_preferences": ["exploration_quests", "space_missions"],
  "observed_learning_difficulties": ["dense_reading_passages", "multi_step_word_problems"],
  "task_management_support": ["visual_checklists", "task_initiation_warmups"],
  "accessibility_preferences": ["opendyslexic_font", "reduced_motion", "high_contrast"],
  "sensory_preferences": {
    "audio_enabled": false,
    "audio_mode": "on_demand",
    "visual_density": "spacious",
    "palette": "soft_calm",
    "animation_level": "none"
  },
  "existing_accommodations": ["extra_time", "visual_instructions", "scheduled_breaks"],
  "caregiver_reported_support_information": ["attention_support"],
  "learner_goals": ["science_mastery", "independent_study_confidence"],
  "consent": {
    "granted": true,
    "timestamp": "2026-09-18T08:00:00Z"
  }
}
```

---

## 5. Non-Diagnostic Privacy Certification

1. **Zero Diagnostic Calculation**: NeuroQuest does **not** evaluate clinical cutoff scores, calculate DSM-5/ICD-10 probability ratings, or produce medical risk classifications.
2. **Pedagogical Sanitization**: LLM mentor prompts are filtered to receive **pedagogical instructions only** (`"Provide step-by-step visual hints and allow extra processing time"`) and are never given clinical diagnostic terms.
3. **Data Sovereignty**: Caregivers can view, modify, or reset the support profile at any time from the settings and caregiver dashboard.
