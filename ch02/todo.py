from fastapi import APIRouter
from model import Todo
todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added succesfully."
    }

@todo_router.get('/todo')
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return { "todo": todo }
    return {
        "message": "Todo with supplied ID doesn't exist.."
    }