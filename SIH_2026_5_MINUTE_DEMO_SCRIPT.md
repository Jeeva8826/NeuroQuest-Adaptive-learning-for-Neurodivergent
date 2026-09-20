# NeuroQuest: 5-Minute SIH 2026 Demonstration Master Script & Execution Playbook

**Competition:** Smart India Hackathon 2026  
**Problem Statement ID:** SIH26207  
**Problem Statement Title:** Student Innovation - Smart Education, a concept that describes learning in digital age. It enables learners to learn more effectively, flexibly and comfortably.  
**Theme:** Smart Education | **Category:** Software  
**Team ID:** 143424 | **Team Name:** ZEUEZ502  
**Target Duration:** Exactly 5:00 Minutes (0:00–2:30 Presentation | 2:30–5:00 Prototype)  
**Core Motto:** *"Same learning objective. Different learning experience."*

---

## 1. Verified Multi-Cloud & System Endpoints

| Resource | Service / Type | Verified Production URL |
| :--- | :--- | :--- |
| **Live Frontend SPA** | Vercel Edge | [`https://neuro-quest-adaptive-learning-for-n.vercel.app/`](https://neuro-quest-adaptive-learning-for-n.vercel.app/) |
| **Live Backend API & ML** | Render Web Service | [`https://neuroquest-adaptive-learning-for.onrender.com/health`](https://neuroquest-adaptive-learning-for.onrender.com/health) |
| **Database & Vector RAG** | Neon Serverless PostgreSQL | `ep-aged-heart-b52ll5dt-pooler...aws.neon.tech/neondb` (26 Tables + PGVector) |
| **Demo Caregiver Account** | Pre-Seeded Auth | **User:** `jeevananth` \| **Password:** `123` (Quick autofill on login page) |
| **Source PPT Presentation** | Official SIH Submission | 6 Verified Slides (Matching `SIH26207` exact submission) |

---

## 2. Minute-by-Minute Demonstration Timeline (5:00 Total)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        NEUROQUEST 5:00 DEMO MASTER TIMELINE                            │
├──────────────┬─────────────────────────────┬───────────────────────────────────────────┤
│ 0:00 - 0:15  │ Slide 1: Project Identity   │ SIH26207, Team ZEUEZ502, Core Philosophy  │
│ 0:15 - 0:55  │ Slide 2: Problem & Solution │ Problems vs. Uniqueness, Feedback Loop    │
│ 0:55 - 1:35  │ Slide 3: Technical Approach │ System Architecture, Tech Stack, ML & BKT │
│ 1:35 - 2:05  │ Slide 4: Feasibility        │ Feasibility vs. Viability, Standout Tech  │
│ 2:05 - 2:25  │ Slide 5: Impact & Benefits  │ Economic & Social Impacts (Diversity)     │
│ 2:25 - 2:30  │ Slide 6: Research Citations │ 2024–2026 Academic Literature Transition  │
├──────────────┼─────────────────────────────┼───────────────────────────────────────────┤
│ 2:30 - 2:45  │ Caretaker Sign-In           │ /login -> Privacy-Safe Caregiver Portal   │
│ 2:45 - 3:00  │ Student Profile             │ Aarav Sharma (Class 7) Accommodations    │
│ 3:00 - 3:20  │ 20-Q Baseline Assessment    │ 10 Educational Dimensions (Zero Medical)  │
│ 3:20 - 3:40  │ Learner Dashboard           │ NCERT Standards 1–10 & Syllabus Modal     │
│ 3:40 - 4:00  │ Lesson & Adaptation         │ Cognitive Friction -> Visual Block Mode   │
│ 4:00 - 4:30  │ Answer Evaluation           │ Real Distractor -> Misconception Diagnosis│
│ 4:30 - 4:50  │ 6-Level Scaffolding & RAG   │ Level 1 Hint, Level 2 Concept, Citations  │
│ 4:50 - 5:00  │ BKT Update & Closing        │ Knowledge Mastery -> "Same Objective..."  │
└──────────────┴─────────────────────────────┴───────────────────────────────────────────┘
```

---

## 3. Spoken Voiceover Script & Visual Actions

### PART 1: PRESENTATION (0:00 – 2:30)

#### [0:00 – 0:15] Slide 1: Identity & Hook
* **Display:** Slide 1 (Smart India Hackathon 2026 — Problem Statement ID: `SIH26207`, Student Innovation - Smart Education, Team ID: `143424`, Team Name: `ZEUEZ502`).
* **Spoken Narrative:**
  > *"Hello everyone. We are Team ZEUEZ502, presenting NeuroQuest for Smart India Hackathon 2026 under Problem Statement SIH26207: Student Innovation - Smart Education.*
  > 
  > *The core idea is simple: the learning objective can remain the same, while the learning experience adapts to the learner."*

---

#### [0:15 – 0:55] Slide 2: Problem, Solution & Uniqueness
* **Display:** Slide 2 (Problems on Left | Solution and Uniqueness on Right | Continuous Feedback Loop at Bottom).
* **Spoken Narrative:**
  > *"Traditional digital learning platforms enforce a rigid, one-size-fits-all paradigm: one interface for every learner, personalization that stops at content recommendations, and assistance that is purely reactive.*
  > 
  > *This creates severe cognitive friction—excessive material, confusing layout, and inflexible pacing leading to cognitive overload and task abandonment. Furthermore, support is fragmented across disconnected tools, and conventional ed-tech often treats neurodivergent learners as deficits to be diagnosed.*
  > 
  > *NeuroQuest completely reimagines this through a closed, learner-driven loop: Learner Profile to Adaptive Learning, Behavioral Evidence, Controlled Adaptation, AI Scaffolding, and Feedback.*
  > 
  > *Importantly, **Neurodiversity is not a Diagnosis**. We never label students. Through an Accessibility-First Interface, learners regulate focus mode, spacing, and chunking. With an Interpretable Learner Model, Dynamic Adaptation, and Grounded RAG Scaffolding, the LLM doesn't just give away answers—it provides clues, explanations, and step-by-step directions.*
  > 
  > *Our continuous feedback loop follows six clear steps: Observe, Interpret, Adapt, Assist, Assess, and Update."*

---

#### [0:55 – 1:35] Slide 3: Technical Approach & Architecture
* **Display:** Slide 3 (Layered System Architecture & Technological Stack).
* **Spoken Narrative:**
  > *"Technically, NeuroQuest is architected across six robust layers.*
  > 
  > *Our **Presentation Layer** is built with React, TypeScript, and Tailwind CSS as an accessible PWA adhering to WCAG 2.2 with multimodal text, audio, and visual controls.*
  > 
  > *The **Application Layer** runs on FastAPI and Python with Pydantic event validation, managing secure JWT authentication, adaptation rules, and background telemetry workers.*
  > 
  > *At the center is our **AI & Learning Intelligence Layer**—the NeuroQuest Core. Here, the rule is strict: **LLM assists, but the Adaptation Engine decides.** It relies solely on learning-relevant signals—because a learning state is never a medical diagnosis. We combine Scikit-learn behavior analysis with Bayesian Knowledge Tracing for skill tracking.*
  > 
  > *Our **Data Layer** couples Neon Serverless PostgreSQL with pgvector for 384-dimensional curriculum embeddings, while Redis handles caching.*
  > 
  > *Deployed on Render and Vercel with automated GitHub Actions, our stack operates with zero-cost sustainability."*

---

#### [1:35 – 2:05] Slide 4: Feasibility & Viability
* **Display:** Slide 4 (Feasibility on Left | Viability on Right | Pre-Existing vs. NeuroQuest Standout at Bottom).
* **Spoken Narrative:**
  > *"On feasibility: NeuroQuest requires no special hardware. It runs on lightweight browser-based APIs like Web Speech and local eye-gaze tracking. By using Bayesian Knowledge Tracing for interpretable assessment, it eliminates expensive deep-learning overhead.*
  > 
  > *On viability: Our cloud architecture enables sustainable AI costs by applying deterministic rules and lightweight machine learning first, reserving LLMs strictly for contextual scaffolding. It easily integrates into Canvas or Moodle via standard LTI.*
  > 
  > *While pre-existing platforms offer isolated adaptive pacing, dialogue tutors, or accessibility toggles, **NeuroQuest stands out** through five pillars: Evidence-Driven adaptation, Contextual AI where every interaction becomes feedback, Learner-Controlled modifications that can always be undone, a Non-Diagnostic label-free approach, and Closed-Loop content-grounded LLM scaffolding."*

---

#### [2:05 – 2:25] Slide 5: Impact & Benefits
* **Display:** Slide 5 (Economic Impacts on Left | Social Impacts and Benefits on Right).
* **Spoken Narrative:**
  > *"Our impact spans both economic and social dimensions.*
  > 
  > *Economically, it delivers scalable personalization supporting multiple learners simultaneously, reduces dropout risk, lowers tool fragmentation, and increases learning efficiency by eliminating time wasted on unsuitable content.*
  > 
  > *Socially, NeuroQuest fosters deep respect for learner diversity. By providing inclusive education and equal learning opportunity, it removes the barriers of one-size-fits-all education. It builds learner independence, reduces frustration through immediate compassionate assistance, and maintains engagement in a calm, stigma-free environment."*

---

#### [2:25 – 2:30] Slide 6: Research Base & Live Transition
* **Display:** Slide 6 (Resources and References — 2024 to 2026 Literature).
* **Spoken Narrative:**
  > *"Our methodology is grounded in recent peer-reviewed research, including 2024 and 2025 systematic reviews on cognitive load in online learning, 25 years of Bayesian Knowledge Tracing, and LLMs in education.*
  > 
  > *Now, let us transition directly to the live NeuroQuest prototype in production."*

---

### PART 2: LIVE PROTOTYPE DEMONSTRATION (2:30 – 5:00)

*Switch active window to the browser tab:* `https://neuro-quest-adaptive-learning-for-n.vercel.app/`

#### [2:30 – 2:45] Caretaker Authentication
* **Screen:** `/login`
* **Action:** Click quick demo login: `jeevananth (Pass: 123)` and click **Sign In Securely**.
* **Spoken Narrative:**
  > *"We log into the caregiver portal. Notice our privacy-first design: zero medical tags, zero clinical deficit jargon. Caregivers have complete visibility over accommodations without stigma."*

---

#### [2:45 – 3:00] Student Profile Inspection
* **Screen:** Caregiver Dashboard (`/caregiver`)
* **Action:** Point out student **Aarav Sharma** (Class 7).
* **Spoken Narrative:**
  > *"Here is Aarav, enrolled in Class 7. His profile is governed strictly by observable educational accommodations: spacious visual density, untimed calm mode, and passion anchors in Space and Robotics."*

---

#### [3:00 – 3:20] 20-Question Baseline Educational Assessment
* **Screen:** `/student-screening/:id`
* **Action:** Show the 20-question questionnaire and the interactive 10-dimension accommodation radar chart.
* **Spoken Narrative:**
  > *"The onboarding baseline uses exactly 20 observable educational questions. Instead of generating a diagnostic label, our backend computes 10 educational support dimensions—calibrating task pacing, font choices, and scaffolding levels automatically."*

---

#### [3:20 – 3:40] Personalized Learner Dashboard & NCERT Catalog
* **Screen:** Learner Portal (`/home` or `/session`)
* **Action:** Showcase the Class 1–10 selector pills and select Class 7 Science Chapter 1: *"Nutrition in Plants"*.
* **Spoken Narrative:**
  > *"Aarav enters his personalized quest arena. The curriculum is authentic NCERT Standard 7 Science, aligned with the National Curriculum Framework and NEP 2020."*

---

#### [3:40 – 4:00] Lesson & Adaptive Interaction (Cognitive Friction Response)
* **Screen:** Active Challenge / Task View
* **Action:** Demonstrate the sensory adaptation toggle or trigger Calm/Focus Mode. Show the notification: *"Switched to Calm Mode — Keep or Undo"*.
* **Spoken Narrative:**
  > *"When complex text creates friction, NeuroQuest observes the signal. Every adaptation is explainable and reversible—telling the learner what changed, why it changed, and providing instant Keep or Undo controls."*

---

#### [4:00 – 4:30] Structured Student Answer Evaluation & Misconception Handling
* **Screen:** Interactive Challenge TaskCard
* **Action:** Submit an incorrect distractor answer (e.g., confusing plant respiration with photosynthesis).
* **Spoken Narrative:**
  > *"When Aarav makes an incorrect selection, there are no red buzzers or deducted points. Our structured pedagogical answer evaluator highlights his choice in rose, detects the authentic NCERT misconception, explains the scientific truth, and offers an immediate retry."*

---

#### [4:30 – 4:50] Graduated 6-Level Scaffolding & Grounded AI
* **Screen:** Scaffold Helper / AI Contextual Assist Box
* **Action:** Click **Request Hint** to step through Level 1 (Hint) and Level 2 (Concept Explanation with visual block).
* **Spoken Narrative:**
  > *"NeuroQuest employs a graduated 6-level hint ladder—from Socratic clarifying questions to parallel worked examples—without prematurely revealing the solution. All AI guidance is grounded via Neon PGVector with verified NCERT textbook citations."*

---

#### [4:50 – 5:00] BKT Learner Update & Core Closing Statement
* **Screen:** Progress & Mastery Bar (`/progress`)
* **Action:** Show the concept mastery progression bar moving from *Exploring* to *Mastered*.
* **Spoken Narrative:**
  > *"With Bayesian Knowledge Tracing updating his mastery state in real time, Aarav achieves genuine curriculum understanding on his own terms.*
  > 
  > *This is NeuroQuest:*  
  > ***Same learning objective. Different learning experience.***  
  > *Thank you."*

---

## 4. Pre-Flight Checklist Before You Press Record

- [x] Slide 1 visible in full-screen mode on screen.
- [x] Browser tab open to `https://neuro-quest-adaptive-learning-for-n.vercel.app/`.
- [x] Microphone positioned and audio input tested.
- [x] Resolution set to 1080p (1920x1080).
- [x] Recording hotkey: **`Win + Alt + R`** (or OBS recording).
