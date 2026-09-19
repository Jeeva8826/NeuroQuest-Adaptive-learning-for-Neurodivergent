from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional, Dict, Any
from bson import ObjectId
import os
import json
from app.models.task import LearningTask
from app.database import get_database
from app.services.auth_service import get_current_user, get_optional_current_user

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

def _load_ncert_syllabus_file():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.normpath(os.path.join(base_dir, "..", "..", "..", "data", "curriculum", "ncert_master_syllabus.json"))
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"standards": []}

@router.get("/syllabus")
async def get_ncert_syllabus(
    grade: Optional[int] = Query(None, ge=1, le=10),
    subject: Optional[str] = Query(None),
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Returns the official NCERT syllabus hierarchy across Standards 1 to 10.
    Can be filtered by grade and subject.
    """
    data = _load_ncert_syllabus_file()
    standards = data.get("standards", [])

    if grade:
        standards = [s for s in standards if s.get("grade") == grade]

    if subject:
        filtered = []
        for s in standards:
            matching_subs = [sub for sub in s.get("subjects", []) if sub.get("subject", "").lower() == subject.lower()]
            if matching_subs:
                s_copy = dict(s)
                s_copy["subjects"] = matching_subs
                filtered.append(s_copy)
        standards = filtered

    return {
        "board": "NCERT",
        "framework": "NEP 2020 / NCF",
        "total_standards": len(standards),
        "standards": standards
    }

@router.get("/standards")
async def get_available_standards(current_user: Optional[dict] = Depends(get_optional_current_user)):
    """
    Returns the list of all available standards and their subject offerings.
    """
    data = _load_ncert_syllabus_file()
    result = []
    for s in data.get("standards", []):
        result.append({
            "grade": s.get("grade"),
            "standard_name": s.get("standard_name"),
            "subjects": [sub.get("subject") for sub in s.get("subjects", [])],
            "total_chapters": sum(len(sub.get("chapters", [])) for sub in s.get("subjects", []))
        })
    return {"standards": result}

@router.get("", response_model=List[LearningTask])
async def get_tasks(
    subject: Optional[str] = Query(None),
    difficulty: Optional[int] = Query(None),
    grade: Optional[int] = Query(None, ge=1, le=10),
    limit: int = Query(50, ge=1, le=200),
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    db = get_database()
    query = {}
    
    if subject:
        query["subject"] = subject
    if difficulty:
        query["difficulty"] = difficulty
    if grade:
        query["$or"] = [{"grade": grade}, {"grade": str(grade)}]

    tasks_cursor = db["tasks"].find(query).limit(limit)
    tasks = await tasks_cursor.to_list(limit)

    # Fallback to broader query if strict grade has no tasks yet
    if not tasks and grade:
        fallback_query = {k: v for k, v in query.items() if k != "$or"}
        tasks = await db["tasks"].find(fallback_query).limit(limit).to_list(limit)
        if not tasks:
            tasks = await db["tasks"].find({}).limit(limit).to_list(limit)

    result = []
    for t in tasks:
        t["id"] = str(t.get("_id", t.get("id", "")))
        result.append(LearningTask(**t))

    return result

@router.get("/{task_id}", response_model=LearningTask)
async def get_task_by_id(task_id: str, current_user: Optional[dict] = Depends(get_optional_current_user)):
    db = get_database()
    try:
        if ObjectId.is_valid(task_id):
            query = {"$or": [{"_id": ObjectId(task_id)}, {"id": task_id}, {"_id": task_id}]}
        else:
            query = {"$or": [{"id": task_id}, {"_id": task_id}]}
    except Exception:
        query = {"$or": [{"id": task_id}, {"_id": task_id}]}
        
    task_doc = await db["tasks"].find_one(query)
    if not task_doc:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
        
    task_doc["id"] = str(task_doc.get("_id", task_id))
    return LearningTask(**task_doc)

