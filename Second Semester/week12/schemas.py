# schemas.py
from pydantic import BaseModel

class Question(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
