# NeuroQuest

NeuroQuest is an accessibility-first, non-diagnostic adaptive learning platform designed for neurodivergent learners. Rather than forcing the learner to adapt to the platform, **NeuroQuest makes the learning experience adapt to the learner.**

Built for the Smart India Hackathon (SIH) 2026.

## Core Philosophy
> **"One learning objective. Multiple ways to reach it."**

NeuroQuest does not attempt to diagnose learners (e.g., "This child has ADHD"). Instead, it identifies learning barriers: *"This learner currently benefits from shorter chunks, visual explanation, slower progression, and guided support."*

## System Architecture

The platform utilizes a continuous learning loop driven by **Bayesian Knowledge Tracing (BKT)** and explicit **Cognitive Load Checks**:

1. **Caregiver Support Profile**: A 20-question profile mapping accessibility preferences (chunking, text density, visuals) rather than medical probability.
2. **Normalized Action Events**: Every interaction is streamed securely into the event engine.
3. **Adaptation Engine**: Uses deterministic rules based on mastery thresholds to adapt content layout and difficulty.
4. **AI/RAG Scaffolding**: Utilizes a 7-level Graduated Scaffold Ladder. When mastery drops, scaffolding increases. The LLM acts strictly within authorized NCERT curriculum data via Retrieval-Augmented Generation (RAG).

## Tech Stack
- **Frontend**: Vite, React, TypeScript, Tailwind CSS, Zustand, Framer Motion
- **Backend**: FastAPI, Python, SQLAlchemy, PostgreSQL, pgvector
- **AI**: Google Gemini (via `google-generativeai`)
- **Testing**: Pytest (Backend), Playwright (E2E)
- **Deployment**: Docker, Docker Compose, GitHub Actions

## Running the Application

### Option 1: Docker Compose (Recommended)
You can launch the entire stack (Frontend, Backend, PostgreSQL) using Docker.

```bash
docker-compose up --build
```
- Frontend: `http://localhost:5173`
- Backend API Docs: `http://localhost:8000/docs`

### Option 2: Local Development

**1. Start the Database**
Ensure PostgreSQL is running locally or via Docker and set your `DATABASE_URL`.

**2. Start the Backend**
```bash
cd backend
python -m venv venv
# Activate the venv
pip install -r requirements.txt
python -m uvicorn run:app --reload
```

**3. Start the Frontend**
```bash
cd frontend
npm install
npm run dev
```

## Data Governance
NeuroQuest explicitly avoids ingesting raw medical/clinical datasets for diagnostic modeling.
The curriculum metadata leverages authorized **NCERT / DIKSHA** resources mapped directly into the Learning Engine schema.
Please see the `data/governance/` directory for our strict Privacy Policy, Dataset Registry, and License tracking.

## Hackathon Demo Flow
Our targeted demo flow showcases the exact moment of UI adaptation:
1. Learner struggles with a dense concept.
2. The UI issues a "Load Check" ("How did that feel?").
3. Learner responds "Too much".
4. The React UI physically transforms the dense text into a sequential, chunked flow with visual icons, and automatically offers graduated hints.
