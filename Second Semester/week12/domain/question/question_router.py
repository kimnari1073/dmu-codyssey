# domain/question/question_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Question

router = APIRouter(prefix="/api/question")


# DB 세션 의존성 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 질문 목록 조회
@router.get("/")
def question_list(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions
