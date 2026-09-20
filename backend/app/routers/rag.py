from fastapi import APIRouter, HTTPException, Query, Depends
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from app.services.rag_service import rag_service
from app.services.auth_service import get_optional_current_user

router = APIRouter(prefix="/api/rag", tags=["Curriculum RAG & PGVector"])

class RAGSearchRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Search query or curriculum concept")
    grade: Optional[int] = Field(None, ge=1, le=10, description="NCERT Standard / Grade filter (1-10)")
    subject: Optional[str] = Field(None, description="Subject filter, e.g. Mathematics, Science")
    top_k: int = Field(5, ge=1, le=50, description="Number of results to retrieve")
    min_score: float = Field(0.0, ge=0.0, le=1.0, description="Minimum relevance score threshold")

class RAGAskRequest(BaseModel):
    question: str = Field(..., min_length=2, description="Student or teacher question")
    grade: Optional[int] = Field(None, ge=1, le=10, description="NCERT Standard filter")
    subject: Optional[str] = Field(None, description="Subject filter")
    learner_interests: Optional[List[str]] = Field(default_factory=lambda: ["space"], description="Learner interests for pedagogical analogies")

@router.get("/status")
async def get_rag_pipeline_status():
    """
    Returns the real-time operational status of the NCERT PGVector & Hybrid RAG Pipeline.
    """
    return rag_service.get_status()

@router.post("/search")
@router.post("/query")
async def search_curriculum_chunks(
    req: RAGSearchRequest,
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Searches NCERT Classes 1–10 curriculum chunks using dense vector embeddings + lexical hybrid ranking.
    """
    results = rag_service.search(
        query=req.query,
        grade=req.grade,
        subject=req.subject,
        top_k=req.top_k,
        min_score=req.min_score
    )
    return {
        "query": req.query,
        "grade_filter": req.grade,
        "subject_filter": req.subject,
        "total_matches": len(results),
        "results": results
    }

@router.post("/ask")
async def ask_grounded_rag(
    req: RAGAskRequest,
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Formulates a pedagogical answer grounded in NCERT curriculum chunks with citations and interest analogies.
    """
    response = rag_service.ask_grounded(
        question=req.question,
        grade=req.grade,
        subject=req.subject,
        learner_interests=req.learner_interests
    )
    return response

@router.get("/chunks")
async def list_curriculum_chunks(
    grade: Optional[int] = Query(None, ge=1, le=10),
    subject: Optional[str] = Query(None),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Lists paginated NCERT curriculum chunks.
    """
    rag_service.init_cache()
    filtered = rag_service._chunks_cache
    if grade is not None:
        filtered = [c for c in filtered if c.get("grade") == grade]
    if subject is not None:
        filtered = [c for c in filtered if subject.lower() in str(c.get("subject", "")).lower()]

    total = len(filtered)
    page_chunks = filtered[offset : offset + limit]

    # Omit raw float vector from simple listing for light payload
    light_chunks = []
    for c in page_chunks:
        c_copy = dict(c)
        c_copy.pop("embedding", None)
        light_chunks.append(c_copy)

    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "chunks": light_chunks
    }

@router.get("/chunks/{chunk_id}")
async def get_single_chunk(
    chunk_id: str,
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Retrieves a single curriculum chunk by its unique ID.
    """
    rag_service.init_cache()
    for c in rag_service._chunks_cache:
        if c.get("chunk_id") == chunk_id:
            c_copy = dict(c)
            c_copy.pop("embedding", None)
            return c_copy
    raise HTTPException(status_code=404, detail=f"Chunk with ID '{chunk_id}' not found.")

@router.post("/sync")
@router.post("/index")
async def sync_chunks_to_pgvector(
    current_user: Optional[dict] = Depends(get_optional_current_user)
):
    """
    Triggers indexing and synchronization of all NCERT Classes 1–10 chunks into PGVector table on Neon.
    """
    res = rag_service.sync_to_pgvector()
    return res
