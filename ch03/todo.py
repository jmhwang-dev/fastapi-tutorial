from fastapi import APIRouter
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []

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