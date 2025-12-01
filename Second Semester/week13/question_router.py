# question_router.py
from fastapi import APIRouter, Depends
from database import get_db
from schemas import Question

router = APIRouter(prefix="/question")


@router.get("/", response_model=list[Question])
def question_list(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, title, content FROM question")
    rows = cursor.fetchall()

    return [
        Question(
            id=row["id"],
            title=row["title"],
            content=row["content"]
        )
        for row in rows
    ]
