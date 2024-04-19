from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []

@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int = Path(..., title="ReDoc에만 나와요", description="ReDoc, Swagger 둘다 나와요")):
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )

@todo_router.get("/todo", response_model=TodoItems)
async def retrive_todo() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo item added successfully."
    }