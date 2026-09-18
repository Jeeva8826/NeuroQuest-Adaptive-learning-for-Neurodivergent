from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from bson import ObjectId
from app.models.task import LearningTask
from app.database import get_database
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

@router.get("", response_model=List[LearningTask])
async def get_tasks(
    subject: Optional[str] = Query(None),
    difficulty: Optional[int] = Query(None),
    limit: int = Query(20, ge=1, le=50),
    current_user: dict = Depends(get_current_user)
):
    db = get_database()
    query = {}
    
    if subject:
        query["subject"] = subject
    if difficulty:
        query["difficulty"] = difficulty

    tasks_cursor = db["tasks"].find(query).limit(limit)
    tasks = await tasks_cursor.to_list(limit)

    result = []
    for t in tasks:
        t["id"] = str(t["_id"])
        result.append(LearningTask(**t))

    return result

@router.get("/{task_id}", response_model=LearningTask)
async def get_task_by_id(task_id: str, current_user: dict = Depends(get_current_user)):
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
