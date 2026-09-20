import os
import json
import re
import math
import logging
import hashlib
from typing import List, Dict, Any, Optional
import numpy as np
from sqlalchemy import text
from app.database import engine, SessionLocal
from app.models.schema import CurriculumChunk

logger = logging.getLogger("neuroquest.rag_service")

# Dimension of curriculum chunk embeddings
VECTOR_DIMENSION = 384

class ZeroCostEmbedder:
    """
    Zero-cost deterministic 384-dimensional semantic embedding generator.
    Requires $0.00, runs completely offline, uses NumPy for fast vectorized
    subword n-gram hashing and pseudo-semantic projection to unit-length vectors.
    """
    def __init__(self, dim: int = VECTOR_DIMENSION):
        self.dim = dim
        # Deterministic projection seeds for consistent vector space
        rng = np.random.RandomState(42)
        self.projection_matrix = rng.normal(0, 1.0, (1024, self.dim))
        # Normalize columns
        self.projection_matrix /= np.linalg.norm(self.projection_matrix, axis=0, keepdims=True)

    def _tokenize_and_hash(self, text_input: str) -> np.ndarray:
        raw_tokens = re.findall(r'\b\w+\b', text_input.lower())
        bow = np.zeros(1024, dtype=np.float32)
        if not raw_tokens:
            return bow

        for token in raw_tokens:
            # Word token hash
            h_word = int(hashlib.md5(token.encode('utf-8')).hexdigest(), 16) % 1024
            bow[h_word] += 1.0
            # Character trigram hashing for morphological/stemming robustness
            if len(token) >= 3:
                for i in range(len(token) - 2):
                    trigram = token[i:i+3]
                    h_tri = int(hashlib.md5(trigram.encode('utf-8')).hexdigest(), 16) % 1024
                    bow[h_tri] += 0.35

        # Sublinear TF scaling
        bow = np.log1p(bow)
        norm = np.linalg.norm(bow)
        if norm > 0:
            bow /= norm
        return bow

    def encode(self, text_input: str) -> List[float]:
        bow = self._tokenize_and_hash(text_input)
        dense = np.dot(bow, self.projection_matrix)
        norm = np.linalg.norm(dense)
        if norm > 0:
            dense = dense / norm
        else:
            dense = np.zeros(self.dim, dtype=np.float32)
        return [float(x) for x in dense]

embedder = ZeroCostEmbedder(VECTOR_DIMENSION)

class RAGService:
    """
    Zero-cost PGVector / Hybrid RAG Pipeline grounded in NCERT Classes 1–10.
    Integrates dense vector similarity via PGVector (or in-memory cosine fallback)
    with lexical keyword matching, grade/standard filtering, and NCERT evidence citations.
    """
    def __init__(self):
        self._chunks_cache: List[Dict[str, Any]] = []
        self._cache_initialized = False

    def _get_project_root(self) -> str:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.abspath(os.path.join(base_dir, "..", "..", ".."))

    def _load_ncert_sources(self) -> Dict[str, Any]:
        root = self._get_project_root()
        kg_path = os.path.join(root, "data", "curriculum", "ncert_knowledge_graph.json")
        syllabus_path = os.path.join(root, "data", "curriculum", "ncert_master_syllabus.json")

        kg_data = {}
        syllabus_data = {}

        if os.path.exists(kg_path):
            try:
                with open(kg_path, "r", encoding="utf-8") as f:
                    kg_data = json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load ncert_knowledge_graph.json: {e}")

        if os.path.exists(syllabus_path):
            try:
                with open(syllabus_path, "r", encoding="utf-8") as f:
                    syllabus_data = json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load ncert_master_syllabus.json: {e}")

        return {"kg": kg_data, "syllabus": syllabus_data}

    def build_curriculum_chunks(self) -> List[Dict[str, Any]]:
        """
        Parses NCERT master syllabus & knowledge graph for Classes 1–10
        and converts concepts and chapters into grounded, searchable chunks.
        """
        sources = self._load_ncert_sources()
        kg = sources["kg"]
        chunks = []

        # 1. Chunks from NCERT Knowledge Graph Concepts
        for sub in kg.get("subjects", []):
            subject_name = sub.get("subject_name", "General")
            for ch in sub.get("chapters", []):
                grade = ch.get("grade", 7)
                standard = ch.get("standard") or f"Class {grade}"
                ch_num = ch.get("chapter_number", 1)
                ch_title = ch.get("title", "")

                for top in ch.get("topics", []):
                    top_title = top.get("title", "")
                    for con in top.get("concepts", []):
                        c_id = con.get("concept_id", "")
                        c_name = con.get("concept_name", "")
                        objs = con.get("learning_objectives", [])
                        obj_str = "; ".join(objs) if isinstance(objs, list) else str(objs)
                        expl = con.get("explanation", {})
                        std_expl = expl.get("standard", "")
                        simp_expl = expl.get("simplified", "")
                        analogies = expl.get("interest_analogies", {})
                        examples = con.get("concrete_examples", [])
                        misconceptions = con.get("common_misconceptions", [])

                        # Build informative text payload for embedding & retrieval
                        text_blocks = [
                            f"Subject: {subject_name}. Standard: {standard}. Chapter {ch_num}: {ch_title}.",
                            f"Topic: {top_title}. Concept: {c_name}.",
                            f"Learning Objective: {obj_str}",
                            f"Concept Definition: {std_expl}",
                            f"Simplified Explanation: {simp_expl}"
                        ]
                        if analogies:
                            analogy_strs = [f"{k.capitalize()} connection: {v}" for k, v in analogies.items()]
                            text_blocks.append("Analogies: " + " | ".join(analogy_strs))
                        if examples:
                            text_blocks.append("Examples: " + "; ".join(examples))
                        if misconceptions:
                            misc_strs = [
                                f"Misconception: {m.get('misconception', '')} -> Scientific Truth: {m.get('scientific_truth', '')}"
                                for m in misconceptions if isinstance(m, dict)
                            ]
                            text_blocks.append("Misconceptions: " + " | ".join(misc_strs))

                        content_text = "\n".join(text_blocks)
                        chunk_id = f"chunk_{standard.replace(' ', '').lower()}_{subject_name[:3].lower()}_{c_id.lower()}"
                        citation = f"NCERT {standard} {subject_name}, Chapter {ch_num}: '{ch_title}'"

                        chunks.append({
                            "chunk_id": chunk_id,
                            "grade": int(grade) if isinstance(grade, (int, str)) and str(grade).isdigit() else 7,
                            "standard": standard,
                            "subject": subject_name,
                            "chapter_number": ch_num,
                            "chapter_title": ch_title,
                            "topic": top_title,
                            "concept_id": c_id,
                            "concept_name": c_name,
                            "learning_objective": obj_str,
                            "content": content_text,
                            "source_reference": citation,
                            "metadata_json": {
                                "simplified_explanation": simp_expl,
                                "interest_analogies": analogies,
                                "concrete_examples": examples,
                                "common_misconceptions": misconceptions,
                                "difficulty": con.get("difficulty", 1.0)
                            }
                        })

        # 2. Add Syllabus Chapter Overviews from ncert_master_syllabus.json
        syllabus = sources["syllabus"]
        for std in syllabus.get("standards", []):
            grade_num = std.get("grade", 1)
            std_name = std.get("standard_name", f"Class {grade_num}")
            for subj_obj in std.get("subjects", []):
                s_name = subj_obj.get("subject", "General")
                textbook = subj_obj.get("textbook", "NCERT Textbook")
                for chap in subj_obj.get("chapters", []):
                    c_num = chap.get("chapter_number", 1)
                    c_title = chap.get("title", "")
                    topics = chap.get("topics", [])
                    outcomes = chap.get("learning_outcomes", [])

                    chunk_id = f"chunk_syl_{std_name.replace(' ', '').lower()}_{s_name[:3].lower()}_ch{c_num}"
                    # Avoid duplicate if already covered with high fidelity
                    if any(c["chunk_id"] == chunk_id for c in chunks):
                        continue

                    content = (
                        f"NCERT Official Syllabus: {std_name} {s_name} ({textbook}).\n"
                        f"Chapter {c_num}: {c_title}.\n"
                        f"Key Topics: {', '.join(topics)}.\n"
                        f"Curriculum Learning Outcomes: {'; '.join(outcomes)}."
                    )
                    citation = f"NCERT Master Curriculum ({std_name} {s_name}, Chapter {c_num}: '{c_title}')"

                    chunks.append({
                        "chunk_id": chunk_id,
                        "grade": grade_num,
                        "standard": std_name,
                        "subject": s_name,
                        "chapter_number": c_num,
                        "chapter_title": c_title,
                        "topic": ", ".join(topics[:3]),
                        "concept_id": f"SYL_{std_name}_{c_num}",
                        "concept_name": c_title,
                        "learning_objective": "; ".join(outcomes),
                        "content": content,
                        "source_reference": citation,
                        "metadata_json": {
                            "textbook": textbook,
                            "topics": topics,
                            "learning_outcomes": outcomes
                        }
                    })

        logger.info(f"Built {len(chunks)} grounded NCERT curriculum chunks across Classes 1–10.")
        return chunks

    def init_cache(self, force_refresh: bool = False):
        if self._cache_initialized and not force_refresh:
            return

        raw_chunks = self.build_curriculum_chunks()
        indexed_chunks = []
        for c in raw_chunks:
            # Generate deterministic 384-dimensional dense embedding
            vec = embedder.encode(c["content"])
            c_copy = dict(c)
            c_copy["embedding"] = vec
            indexed_chunks.append(c_copy)

        self._chunks_cache = indexed_chunks
        self._cache_initialized = True
        logger.info(f"RAGService cached {len(self._chunks_cache)} embedded NCERT curriculum chunks.")

    def sync_to_pgvector(self) -> Dict[str, Any]:
        """
        Persists and synchronizes curriculum chunks into the Neon PostgreSQL
        `curriculum_chunks` table with pgvector embeddings.
        """
        self.init_cache()
        if engine is None or SessionLocal is None:
            return {
                "status": "in_memory_only",
                "message": "Database engine unavailable, running with in-memory PGVector-compatible store",
                "synced_count": len(self._chunks_cache)
            }

        synced = 0
        errors = 0
        db = SessionLocal()
        try:
            # Ensure extension exists
            try:
                db.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
                db.commit()
            except Exception as e:
                db.rollback()
                logger.warning(f"Notice on vector extension: {e}")

            for c in self._chunks_cache:
                try:
                    existing = db.query(CurriculumChunk).filter(CurriculumChunk.chunk_id == c["chunk_id"]).first()
                    if not existing:
                        new_chunk = CurriculumChunk(
                            chunk_id=c["chunk_id"],
                            grade=c["grade"],
                            standard=c["standard"],
                            subject=c["subject"],
                            chapter_number=c["chapter_number"],
                            chapter_title=c["chapter_title"],
                            topic=c["topic"],
                            concept_id=c["concept_id"],
                            concept_name=c["concept_name"],
                            learning_objective=c["learning_objective"],
                            content=c["content"],
                            source_reference=c["source_reference"],
                            metadata_json=c["metadata_json"],
                            embedding=c["embedding"]
                        )
                        db.add(new_chunk)
                        synced += 1
                except Exception as inner_e:
                    errors += 1
                    logger.debug(f"Row sync note for {c['chunk_id']}: {inner_e}")

            db.commit()
            total_in_db = db.query(CurriculumChunk).count()
            logger.info(f"PGVector sync complete: {synced} new chunks added, {total_in_db} total in database.")
            return {
                "status": "success",
                "synced_count": synced,
                "total_in_database": total_in_db,
                "vector_dimension": VECTOR_DIMENSION,
                "engine": "Neon Serverless PostgreSQL (pgvector)"
            }
        except Exception as e:
            db.rollback()
            logger.error(f"Error syncing chunks to PGVector: {e}")
            return {
                "status": "partial_fallback",
                "error": str(e),
                "in_memory_count": len(self._chunks_cache)
            }
        finally:
            db.close()

    def search(
        self,
        query: str,
        grade: Optional[int] = None,
        subject: Optional[str] = None,
        top_k: int = 5,
        min_score: float = 0.0
    ) -> List[Dict[str, Any]]:
        """
        Executes hybrid dense vector + lexical retrieval grounded in NCERT syllabus.
        Combines 60% semantic cosine similarity with 40% lexical/keyword match.
        """
        self.init_cache()
        if not self._chunks_cache:
            return []

        query_vec = np.array(embedder.encode(query), dtype=np.float32)
        query_words = set(re.findall(r'\b\w+\b', query.lower()))

        scored_results = []
        for chunk in self._chunks_cache:
            # Metadata filtering
            if grade is not None and chunk.get("grade") != grade:
                continue
            if subject is not None and subject.lower() not in str(chunk.get("subject", "")).lower():
                continue

            # 1. Dense Semantic Cosine Similarity
            c_vec = np.array(chunk["embedding"], dtype=np.float32)
            norm_product = (np.linalg.norm(query_vec) * np.linalg.norm(c_vec))
            cos_sim = float(np.dot(query_vec, c_vec) / norm_product) if norm_product > 0 else 0.0

            # 2. Lexical / Keyword Token Overlap (BM25 surrogate)
            content_words = set(re.findall(r'\b\w+\b', chunk["content"].lower()))
            topic_words = set(re.findall(r'\b\w+\b', f"{chunk.get('concept_name', '')} {chunk.get('topic', '')}".lower()))

            overlap_content = len(query_words & content_words)
            overlap_topic = len(query_words & topic_words)
            lexical_score = min(1.0, (overlap_content * 0.15) + (overlap_topic * 0.35))

            # 3. Hybrid Score Combination
            hybrid_score = (0.60 * max(0.0, cos_sim)) + (0.40 * lexical_score)

            if hybrid_score >= min_score:
                scored_results.append({
                    "chunk_id": chunk["chunk_id"],
                    "grade": chunk["grade"],
                    "standard": chunk["standard"],
                    "subject": chunk["subject"],
                    "chapter_number": chunk["chapter_number"],
                    "chapter_title": chunk["chapter_title"],
                    "topic": chunk["topic"],
                    "concept_id": chunk["concept_id"],
                    "concept_name": chunk["concept_name"],
                    "learning_objective": chunk["learning_objective"],
                    "content": chunk["content"],
                    "source_reference": chunk["source_reference"],
                    "metadata": chunk["metadata_json"],
                    "score": round(float(hybrid_score), 4),
                    "cosine_similarity": round(float(cos_sim), 4),
                    "lexical_overlap": round(float(lexical_score), 4),
                    "citation": chunk["source_reference"]
                })

        scored_results.sort(key=lambda x: x["score"], reverse=True)
        return scored_results[:top_k]

    def ask_grounded(
        self,
        question: str,
        grade: Optional[int] = None,
        subject: Optional[str] = None,
        learner_interests: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Retrieves grounded NCERT evidence chunks and formulates an educational,
        interest-tailored, non-punitive answer citing textbook sources.
        """
        evidence_chunks = self.search(question, grade=grade, subject=subject, top_k=3)
        if not evidence_chunks:
            # Retry without grade restriction if narrow search missed
            evidence_chunks = self.search(question, top_k=3)

        interests = learner_interests or ["space"]
        primary_interest = str(interests[0]).lower() if interests else "space"

        if evidence_chunks:
            top_chunk = evidence_chunks[0]
            metadata = top_chunk.get("metadata", {})
            simplified = metadata.get("simplified_explanation") or top_chunk.get("content", "").split("\n")[0]
            analogies = metadata.get("interest_analogies", {})
            analogy_text = analogies.get(primary_interest) or analogies.get("space") or ""

            answer_parts = [
                f"Based on {top_chunk['citation']}:",
                f"{simplified}"
            ]
            if analogy_text:
                answer_parts.append(f"Here is a cool {primary_interest.capitalize()} connection: {analogy_text}")

            citations = list({c["citation"] for c in evidence_chunks})

            return {
                "question": question,
                "answer": "\n\n".join(answer_parts),
                "grounded": True,
                "confidence_score": top_chunk["score"],
                "concept_id": top_chunk.get("concept_id"),
                "concept_name": top_chunk.get("concept_name"),
                "chapter": f"Chapter {top_chunk.get('chapter_number')}: {top_chunk.get('chapter_title')}",
                "citations": citations,
                "evidence_chunks": evidence_chunks
            }
        else:
            return {
                "question": question,
                "answer": "Let's explore this step-by-step together! The NCERT curriculum emphasizes hands-on inquiry.",
                "grounded": False,
                "confidence_score": 0.0,
                "concept_id": None,
                "concept_name": None,
                "chapter": None,
                "citations": ["NCERT Master Syllabus (Classes 1–10)"],
                "evidence_chunks": []
            }

    def get_status(self) -> Dict[str, Any]:
        self.init_cache()
        db_count = 0
        db_connected = False
        if engine is not None and SessionLocal is not None:
            try:
                db = SessionLocal()
                db_count = db.query(CurriculumChunk).count()
                db_connected = True
                db.close()
            except Exception:
                pass

        return {
            "status": "operational",
            "pipeline": "Zero-Cost PGVector / Hybrid RAG",
            "vector_dimension": VECTOR_DIMENSION,
            "in_memory_cached_chunks": len(self._chunks_cache),
            "neon_pgvector_active": db_connected,
            "neon_stored_chunks": db_count,
            "classes_covered": "NCERT Standards 1–10",
            "subjects_indexed": ["Mathematics", "Science", "Environmental Studies (EVS)"],
            "embedding_type": "Deterministic Dense Subword Projection (Zero-Cost, Offline-Ready)"
        }

rag_service = RAGService()
