# main.py
from database import SessionLocal
from models import Question

db = SessionLocal()

new_q = Question(
    subject="테스트 제목",
    content="테스트 내용"
)

db.add(new_q)
db.commit()

print("INSERT 완료")
