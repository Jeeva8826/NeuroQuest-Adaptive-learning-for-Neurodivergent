# NeuroQuest: Project Blueprint & Technical Summary

> [!NOTE]
> This document serves as the master blueprint for **NeuroQuest** — an AI Adaptive Learning Platform designed specifically for neurodivergent learners. It encapsulates everything built so far, from the tech stack to core engines, allowing you to recreate or continue this project from scratch in a new environment.

## 1. Project Overview & Mission
**NeuroQuest** is an adaptive, gamified learning platform tailored to accommodate the sensory and cognitive needs of neurodivergent learners (e.g., ADHD, Autism, Dyslexia, Sensory Processing Disorder). Instead of static learning modules, it utilizes a machine-learning backend to track real-time telemetry (mouse movements, idle time, simulated gaze) to infer the learner's cognitive state (e.g., *Focused*, *Attention Drift*, *Fatigue*) and dynamically adapts the UI and difficulty.

---

## 2. Technology Stack

### 🖥️ Frontend (Client)
- **Framework:** React 18 (Bootstrapped with Vite)
- **Styling:** Tailwind CSS (for rapid, responsive, and adaptive styling)
- **Routing:** React Router DOM v6
- **HTTP Client:** Axios (configured with JWT interceptors)
- **Icons:** Lucide React
- **State Management:** React Context APIs (`AuthContext`, `ThemeContext`, `SensoryContext`)

### ⚙️ Backend (Server)
- **Framework:** FastAPI (Python)
- **Server:** Uvicorn (Running on `127.0.0.1:8000`)
- **Validation:** Pydantic (v2) with `email-validator`
- **Authentication:** JWT (JSON Web Tokens) with `passlib` (bcrypt password hashing)
- **Machine Learning:** `scikit-learn`, `pandas`, `numpy`, `joblib`
- **Data Fetching (AI Fallback):** `httpx`, `requests`

### 🗄️ Database
- **Database:** MongoDB (Local instance at `mongodb://localhost:27017`)
- **ODM / Driver:** Motor (AsyncIOMotorClient)

---

## 3. Core Engines & Features Implemented

### 🧠 Machine Learning & Adaptation Engine
- **Scikit-Learn Learner State ML Model:** A custom trained model (`learner_state_model.joblib`) that processes real-time session telemetry (click rate, gaze drift, idle ratio, response time) to predict the learner's current state (e.g., `FOCUSED`, `ATTENTION_DRIFT`, `POSSIBLE_FATIGUE`).
- **Real-Time Session Adaptation Engine:** Automatically adjusts the frontend UI based on the ML predictions (e.g., switching to a "calm" UI mode during fatigue, or a "focus" UI mode during attention drift).

### 👤 User Onboarding & Profiling
- **Caregiver Discovery Questionnaire:** A dual-role system (`caregiver` and `learner`). Caregivers create accounts, set up their learner's profile, and select primary conditions (ADHD, Autism, etc.).
- **Medical & Preferences Onboarding:** Collects detailed visual and sensory preferences (background themes like "Space", "Animals", "Coding") and motivation styles (Reward vs. Collection).

### 🎮 Gamification & Session Mechanics
- **Personal Game World & Non-Competitive Mastery Tree:** A stress-free gamified environment where learners earn stars and unlock items for their personal vault rather than competing against peers.
- **Adaptive Difficulty & Failure Scaffolding Engine:** When a learner submits an incorrect answer, the system does not punish them. Instead, it triggers AI-generated scaffolding (hints and encouragement) to gently guide them to the correct answer.
- **AI Mentor & Personalized Tasks:** Dynamically generates custom tasks based on the learner's current subject focus and difficulty level.

### 📊 Dashboards & Demo Tools
- **Caregiver Insights Dashboard:** Provides parents/caregivers with detailed insights into the learner's progress, cognitive states, and task completion metrics.
- **Hackathon Demo Engine:** A specialized toolbar built for presentations that allows instant activation of demo profiles (Learner A, B, C) and manual simulation of cognitive states (e.g., forcing a "Fatigue" state) to instantly demonstrate the UI adaptation.

---

## 4. Architecture & Directory Structure

### Backend Structure (`/backend`)
```text
backend/
├── app/
│   ├── ml/                 # ML Models, Training Scripts, Prediction Service
│   ├── models/             # Pydantic Data Models (user, tasks, session, progress)
│   ├── routers/            # FastAPI Endpoints (auth, telemetry, session, demo, etc.)
│   ├── services/           # Business logic, DB seeding, Auth utils
│   ├── main.py             # FastAPI App Initialization & CORS
│   └── database.py         # MongoDB Motor Connection Setup
├── test_final_demo.py      # Automated Hackathon Demo Test Suite
├── requirements.txt        # Python Dependencies
└── run.py                  # Uvicorn entry point
```

### Frontend Structure (`/frontend`)
```text
frontend/
├── src/
│   ├── components/         # Reusable UI (Navbar, Session components, Task cards)
│   ├── context/            # React Contexts (Auth, Theme, Sensory state)
│   ├── pages/              # Route Pages (SessionPage, CaregiverDashboard, etc.)
│   ├── services/           # Axios API wrappers (api.js, telemetryService.js)
│   ├── App.jsx             # Main Router and Route Guards
│   └── main.jsx            # React DOM Root
├── package.json            # Node Dependencies
├── tailwind.config.js      # Tailwind Theme Configuration
└── vite.config.js          # Vite Config (includes /api proxy to backend)
```

---

## 5. Environment Setup & Execution Guide

If you are setting this up from scratch in a new environment, follow these steps:

> [!IMPORTANT]
> **Prerequisite:** Ensure **MongoDB Community Server** is installed and actively running on your machine at port `27017`. Without this, the backend will fail to start.

### Step 1: Start the Backend
1. Open a terminal and navigate to the `backend` directory.
2. Create and activate a Python virtual environment.
3. Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure `email-validator` is included in the requirements, as Pydantic's `EmailStr` depends on it).*
4. Run the server:
   ```bash
   python run.py
   ```
   *The FastAPI server will start on `http://127.0.0.1:8000` and automatically seed the MongoDB database.*

### Step 2: Start the Frontend
1. Open a separate terminal and navigate to the `frontend` directory.
2. Install node modules:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   *The React app will be accessible at `http://localhost:3000`. Vite is configured to proxy all `/api` requests to the backend.*

---

## 6. Known Quirks / Resuming Work
- **MongoDB Dependency:** The backend will intentionally crash on startup if it cannot connect to MongoDB. Always start the database service first.
- **Demo Mode:** If you need to quickly test the application without going through full registration, utilize the `/api/demo/profiles` endpoints or the "Hackathon Demo Bar" in the frontend to instantly mock a user state.
- **Telemetry Loop:** The frontend `telemetryService.js` simulates gaze and interaction data if a webcam is not available, feeding this to the backend ML model to trigger UI adaptations.
