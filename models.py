# models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError

# ---- DATABASE SETUP ----
engine = create_engine("sqlite:///users.db", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

# ---- MODEL ----
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    secret_question = Column(String, nullable=False)
    secret_answer = Column(String, nullable=False)

# ---- CRUD ----
def create_user(username, password, secret_q, secret_a):
    db = SessionLocal()
    user = User(
        username=username,
        password=password,
        secret_question=secret_q,
        secret_answer=secret_a
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        return None
    finally:
        db.close()

# ---- CREATE TABLES ----
Base.metadata.create_all(bind=engine)
