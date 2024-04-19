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

@todo_router.put('/todo/{todo_id}')
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }
    
    return {
        "message": "Todo with supplied ID doesn't exits."
    }

@todo_router.delete('/todo/{todo_id}')
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    return {
        "message": "Todo with suppliced ID doesn't exist."
    }