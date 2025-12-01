from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    description: str


# 수정용 모델
class TodoItem(BaseModel):
    title: str
    description: str
