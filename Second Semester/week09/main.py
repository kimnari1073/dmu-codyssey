from fastapi import FastAPI, HTTPException
from model import Todo, TodoItem

app = FastAPI()

# 인메모리 todo 목록
todos = {
    1: {"id": 1, "title": "Prepare oxygen tank", "description": "Check pressure and refill"},
    2: {"id": 2, "title": "Repair rover", "description": "Fix wheel alignment"},
}


# 전체 조회
@app.get("/todo")
def get_all_todos():
    return list(todos.values())


# 개별 조회
@app.get("/todo/{todo_id}")
def get_single_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


# 추가 (참고용)
@app.post("/todo")
def create_todo(todo: Todo):
    todos[todo.id] = todo.dict()
    return todos[todo.id]


# 수정
@app.put("/todo/{todo_id}")
def update_todo(todo_id: int, todo_item: TodoItem):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")

    todos[todo_id]["title"] = todo_item.title
    todos[todo_id]["description"] = todo_item.description

    return todos[todo_id]


# 삭제
@app.delete("/todo/{todo_id}")
def delete_single_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")

    deleted = todos.pop(todo_id)
    return deleted
