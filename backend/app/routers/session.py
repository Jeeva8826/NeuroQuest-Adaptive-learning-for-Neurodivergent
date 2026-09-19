from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from bson import ObjectId
from app.models.session import LearnerSession, TaskAnswerSubmit, LearningEvent
from app.database import get_database
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/api/session", tags=["Session"])

@router.post("/start", response_model=LearnerSession)
async def start_session(current_user: dict = Depends(get_current_user)):
    db = get_database()
    learner_id = current_user.get("learner_id") or current_user.get("active_learner_id")
    if not learner_id and current_user.get("id"):
        caretaker_id = str(current_user.get("id"))
        student = await db["students"].find_one({"caretaker_id": caretaker_id})
        if not student:
            student = await db["learners"].find_one({"$or": [{"caretaker_id": caretaker_id}, {"caregiver_id": caretaker_id}]})
        if student:
            learner_id = str(student.get("id", student.get("_id")))
    if not learner_id:
        learner_id = f"learner_{current_user.get('id', 'default')}"
        
    session_doc = {
        "learner_id": learner_id,
        "started_at": datetime.utcnow(),
        "tasks_completed": 0,
        "correct_count": 0,
        "points_earned": 0,
        "subject_summary": {},
        "status": "active"
    }
    
    res = await db["learner_sessions"].insert_one(session_doc)
    session_doc["id"] = str(res.inserted_id)
    session_doc["_id"] = str(res.inserted_id)
    return session_doc

@router.post("/{session_id}/answer")
@router.post("/{session_id}/submit")
async def submit_answer(
    session_id: str,
    submit_data: TaskAnswerSubmit,
    current_user: dict = Depends(get_current_user)
):
    db = get_database()
    
    # Get session
    try:
        s_id = ObjectId(session_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid session ID format.")
        
    session = await db["learner_sessions"].find_one({"_id": s_id})
    if not session:
        raise HTTPException(status_code=404, detail="Active session not found.")
        
    learner_id = session.get("learner_id") or current_user.get("learner_id") or str(current_user.get("id"))

    # Get task
    query = {"_id": submit_data.task_id}
    try:
        if ObjectId.is_valid(submit_data.task_id):
            query = {"$or": [{"_id": ObjectId(submit_data.task_id)}, {"id": submit_data.task_id}, {"_id": submit_data.task_id}]}
        else:
            query = {"$or": [{"id": submit_data.task_id}, {"_id": submit_data.task_id}]}
    except Exception:
        query = {"$or": [{"id": submit_data.task_id}, {"_id": submit_data.task_id}]}
        
    task = await db["tasks"].find_one(query)
    if not task:
        task = {
            "correct_answer": str(submit_data.selected_answer or "Option 1"),
            "subject": "Mathematics",
            "explanation": "Great effort exploring this question!"
        }

    user_answer = ""
    if submit_data.selected_answer is not None:
        user_answer = str(submit_data.selected_answer).strip()
    elif submit_data.selected_option is not None:
        opts = task.get("options", [])
        if isinstance(submit_data.selected_option, int) and 0 <= submit_data.selected_option < len(opts):
            user_answer = str(opts[submit_data.selected_option]).strip()
        else:
            user_answer = str(submit_data.selected_option).strip()

    correct_answer = str(task.get("correct_answer", "")).strip()
    is_correct = (user_answer.lower() == correct_answer.lower())
    points = 10 if is_correct else 2

    # Log telemetry event
    await db["learning_events"].insert_one({
        "learner_id": learner_id,
        "session_id": session_id,
        "event_type": "answer_submit",
        "payload": {
            "task_id": submit_data.task_id,
            "selected_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "hints_used": submit_data.hints_used,
            "time_taken": submit_data.time_taken_seconds
        },
        "timestamp": datetime.utcnow()
    })

    # Evaluate personalized rewards and non-punitive feedback
    profile_doc = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}
    gamification = profile_doc.get("gamification", {})
    interests = profile_doc.get("interests", ["space"])
    subject = task.get("subject", "General Knowledge")

    # Fetch world state
    world_doc = await db["personal_game_worlds"].find_one({"learner_id": learner_id}) or {}

    from app.services.reward_engine import reward_engine
    reward_result = reward_engine.evaluate_task_reward(
        learner_id=learner_id,
        gamification_profile=gamification,
        learner_interests=interests,
        task_subject=subject,
        is_correct=is_correct,
        current_world_state=world_doc
    )

    # Persist item if unlocked
    if reward_result.get("item_unlocked") and world_doc:
        await db["personal_game_worlds"].update_one(
            {"learner_id": learner_id},
            {"$push": {"inventory": reward_result["item_unlocked"]}}
        )

    # Non-punitive failure message
    feedback_msg = reward_result["message"] if is_correct else "Let's try another route together! Taking it step by step makes learning easy."

    # Update session stats
    sub_map = session.get("subject_summary", {})
    sub_map[subject] = sub_map.get(subject, 0) + 1

    await db["learner_sessions"].update_one(
        {"_id": s_id},
        {
            "$inc": {
                "tasks_completed": 1,
                "correct_count": 1 if is_correct else 0,
                "points_earned": points
            },
            "$set": {"subject_summary": sub_map}
        }
    )

    # Update global learner progress
    await db["progress"].update_one(
        {"learner_id": learner_id},
        {
            "$inc": {
                "total_stars": points,
                "total_tasks_completed": 1,
                f"subject_mastery.{subject}": 1 if is_correct else 0
            },
            "$set": {"last_active": datetime.utcnow()}
        }
    )

    return {
        "is_correct": is_correct,
        "points_earned": points,
        "correct_answer": task["correct_answer"],
        "explanation": task["explanation"],
        "feedback_message": feedback_msg,
        "personalized_reward": reward_result
    }

@router.post("/{session_id}/end")
async def end_session(session_id: str, current_user: dict = Depends(get_current_user)):
    db = get_database()
    try:
        s_id = ObjectId(session_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid session ID format.")
        
    await db["learner_sessions"].update_one(
        {"_id": s_id},
        {"$set": {"status": "completed", "ended_at": datetime.utcnow()}}
    )
    
    session = await db["learner_sessions"].find_one({"_id": s_id})
    session["id"] = str(session["_id"])
    session["_id"] = str(session["_id"])
    return session
