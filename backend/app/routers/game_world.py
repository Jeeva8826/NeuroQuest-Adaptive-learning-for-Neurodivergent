from fastapi import APIRouter, HTTPException, Depends
from app.services.auth_service import get_current_user
from app.database import get_database
from app.services.game_world_service import game_world_service

router = APIRouter(prefix="/api/game-world", tags=["Personal Game World"])

@router.get("")
async def get_personal_game_world(current_user: dict = Depends(get_current_user)):
    db = get_database()
    learner_id = current_user.get("learner_id")
    if not learner_id:
        raise HTTPException(status_code=400, detail="No learner found.")
        
    profile = await db["learner_preferences"].find_one({"learner_id": learner_id}) or {}
    world_doc = await game_world_service.get_or_create_game_world(learner_id, profile)
    if "_id" in world_doc:
        world_doc["id"] = str(world_doc["_id"])
        del world_doc["_id"]
    return world_doc

@router.get("/mastery-tree")
async def get_personal_mastery_tree(current_user: dict = Depends(get_current_user)):
    learner_id = current_user.get("learner_id")
    if not learner_id:
        raise HTTPException(status_code=400, detail="No learner found.")
        
    tree_doc = await game_world_service.get_or_create_mastery_tree(learner_id)
    if "_id" in tree_doc:
        tree_doc["id"] = str(tree_doc["_id"])
        del tree_doc["_id"]
    return tree_doc
