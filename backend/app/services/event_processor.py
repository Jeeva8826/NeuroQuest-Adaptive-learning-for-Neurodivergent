from typing import Any, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.schema import LearningEvent, QuestionAttempt, LearnerMastery, Learner
from app.services.bkt import update_bkt_mastery

class NormalizedActionProcessor:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def process_event(self, learner_id: int, event_type: str, payload: Dict[str, Any]):
        # 1. Log the event
        event = LearningEvent(
            learner_id=learner_id,
            event_type=event_type,
            payload=payload
        )
        self.db.add(event)
        await self.db.flush()

        # 2. Extract common fields
        action = payload.get("action")
        
        # 3. Handle question attempts specifically for BKT
        if event_type == "QUESTION_ATTEMPT":
            is_correct = payload.get("is_correct", False)
            variant_id = payload.get("variant_id")
            concept_id = payload.get("concept_id")
            
            attempt = QuestionAttempt(
                event_id=event.id,
                variant_id=variant_id,
                is_correct=is_correct,
                response_time_ms=payload.get("response_time_ms", 0)
            )
            self.db.add(attempt)
            
            if concept_id:
                await update_bkt_mastery(self.db, learner_id, concept_id, is_correct)
                
        # Commit the transaction
        await self.db.commit()
        return event

