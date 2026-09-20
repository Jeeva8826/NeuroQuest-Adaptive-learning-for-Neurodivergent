from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, JSON, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from app.database import Base
import enum

class UserRole(str, enum.Enum):
    CAREGIVER = "CAREGIVER"
    EDUCATOR = "EDUCATOR"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CAREGIVER)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    learners = relationship("Learner", back_populates="caregiver")
    caregiver_profile = relationship("CaregiverProfile", back_populates="user", uselist=False)

class Learner(Base):
    __tablename__ = "learners"
    id = Column(Integer, primary_key=True, index=True)
    caregiver_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    date_of_birth = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    caregiver = relationship("User", back_populates="learners")
    support_preferences = relationship("SupportPreference", back_populates="learner", uselist=False)
    mastery = relationship("LearnerMastery", back_populates="learner")
    events = relationship("LearningEvent", back_populates="learner")

class CaregiverProfile(Base):
    __tablename__ = "caregiver_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    questionnaire_completed = Column(Boolean, default=False)
    questionnaire_responses = Column(JSON)
    
    user = relationship("User", back_populates="caregiver_profile")

class SupportPreference(Base):
    __tablename__ = "support_preferences"
    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("learners.id"))
    visual_support_level = Column(Integer)
    audio_support_level = Column(Integer)
    repetition_needs = Column(Integer)
    feedback_style = Column(String)
    sensory_preferences = Column(JSON)
    
    learner = relationship("Learner", back_populates="support_preferences")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(Text)
    
    chapters = relationship("Chapter", back_populates="subject")

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    title = Column(String)
    order_index = Column(Integer)
    
    subject = relationship("Subject", back_populates="chapters")
    concepts = relationship("Concept", back_populates="chapter")

class Concept(Base):
    __tablename__ = "concepts"
    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    name = Column(String)
    description = Column(Text)
    difficulty_level = Column(Float)
    
    chapter = relationship("Chapter", back_populates="concepts")
    prerequisites = relationship("ConceptPrerequisite", foreign_keys="ConceptPrerequisite.concept_id", back_populates="concept")
    objectives = relationship("LearningObjective", back_populates="concept")

class ConceptPrerequisite(Base):
    __tablename__ = "concept_prerequisites"
    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(Integer, ForeignKey("concepts.id"))
    prerequisite_id = Column(Integer, ForeignKey("concepts.id"))
    
    concept = relationship("Concept", foreign_keys=[concept_id], back_populates="prerequisites")
    prerequisite = relationship("Concept", foreign_keys=[prerequisite_id])

class LearningObjective(Base):
    __tablename__ = "learning_objectives"
    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(Integer, ForeignKey("concepts.id"))
    description = Column(Text)
    
    concept = relationship("Concept", back_populates="objectives")
    questions = relationship("Question", back_populates="objective")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    objective_id = Column(Integer, ForeignKey("learning_objectives.id"))
    base_text = Column(Text)
    question_type = Column(String)
    difficulty = Column(Float)
    
    objective = relationship("LearningObjective", back_populates="questions")
    variants = relationship("QuestionVariant", back_populates="question")

class QuestionVariant(Base):
    __tablename__ = "question_variants"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    content = Column(JSON)
    sensory_adaptation = Column(String)
    
    question = relationship("Question", back_populates="variants")

class LearnerMastery(Base):
    __tablename__ = "learner_mastery"
    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("learners.id"))
    concept_id = Column(Integer, ForeignKey("concepts.id"))
    p_known = Column(Float, default=0.1)
    p_guess = Column(Float, default=0.2)
    p_slip = Column(Float, default=0.1)
    p_transit = Column(Float, default=0.1)
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    learner = relationship("Learner", back_populates="mastery")

class LearningEvent(Base):
    __tablename__ = "learning_events"
    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("learners.id"))
    event_type = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    payload = Column(JSON)
    
    learner = relationship("Learner", back_populates="events")

class QuestionAttempt(Base):
    __tablename__ = "question_attempts"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("learning_events.id"))
    variant_id = Column(Integer, ForeignKey("question_variants.id"))
    is_correct = Column(Boolean)
    response_time_ms = Column(Integer)
    
    event = relationship("LearningEvent")

class Adaptation(Base):
    __tablename__ = "adaptations"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("learning_events.id"))
    adaptation_type = Column(String)
    applied_changes = Column(JSON)

class AdaptationFeedback(Base):
    __tablename__ = "adaptation_feedback"
    id = Column(Integer, primary_key=True, index=True)
    adaptation_id = Column(Integer, ForeignKey("adaptations.id"))
    success_rating = Column(Float)

class Scaffold(Base):
    __tablename__ = "scaffolds"
    id = Column(Integer, primary_key=True, index=True)
    variant_id = Column(Integer, ForeignKey("question_variants.id"))
    scaffold_level = Column(Integer)
    content = Column(JSON)

class GameSession(Base):
    __tablename__ = "game_sessions"
    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("learners.id"))
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    ended_at = Column(DateTime(timezone=True))
    device_info = Column(JSON)

class GameEvent(Base):
    __tablename__ = "game_events"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("game_sessions.id"))
    action_type = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    event_data = Column(JSON)

class ContentSource(Base):
    __tablename__ = "content_sources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    url = Column(String)

class ContentLicense(Base):
    __tablename__ = "content_licenses"
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("content_sources.id"))
    license_type = Column(String)

class CurriculumChunk(Base):
    __tablename__ = "curriculum_chunks"
    id = Column(Integer, primary_key=True, index=True)
    chunk_id = Column(String, unique=True, index=True)
    grade = Column(Integer, index=True)
    standard = Column(String, index=True)
    subject = Column(String, index=True)
    chapter_number = Column(Integer)
    chapter_title = Column(String, index=True)
    topic = Column(String)
    concept_id = Column(String, index=True)
    concept_name = Column(String)
    learning_objective = Column(Text)
    content = Column(Text, nullable=False)
    source_reference = Column(String)
    metadata_json = Column(JSON, default=dict)
    embedding = Column(Vector(384), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

