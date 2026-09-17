import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add backend directory to path so we can import app models
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

try:
    from app.models.schema import Base, User, UserRole, Learner, Concept, Question
    from app.config import settings
    from passlib.context import CryptContext
except ImportError as e:
    print(f"Warning: Could not import backend schema: {e}")
    sys.exit(1)

DATABASE_URL = settings.DATABASE_URL
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def seed():
    print(f"Using database URL: {DATABASE_URL}")
    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)

    print("Initializing database schema...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    print("Seeding database with test credentials and dummy data...")
    with Session() as session:
        # Create Test Caregiver User
        caregiver_user = User(
            username="testparent",
            email="testparent@example.com",
            hashed_password=get_password_hash("testpassword"),
            role=UserRole.CAREGIVER
        )
        session.add(caregiver_user)
        session.commit()
        session.refresh(caregiver_user)

        # Create Test Learner
        learner = Learner(
            caregiver_id=caregiver_user.id,
            name="Test Learner"
        )
        session.add(learner)
        session.commit()

        # Create test concept
        concept = Concept(
            name="Photosynthesis - Food Making Process in Plants"
        )
        session.add(concept)
        session.commit()
        session.refresh(concept)

        print("[OK] Test Credentials Generated:\nUsername: testparent\nPassword: testpassword\n")

if __name__ == "__main__":
    seed()
