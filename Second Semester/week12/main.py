# main.py
from fastapi import FastAPI
from database import SessionLocal
from models import Question
from datetime import datetime

app = FastAPI()

@app.get("/create_test")
def create_test():
    db = SessionLocal()
    q = Question(
        subject="테스트 질문",
        content="DB 동작 확인용",
        create_date=datetime.utcnow()
    )
    db.add(q)
    db.commit()
    db.refresh(q)
    return q
