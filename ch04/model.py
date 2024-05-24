from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel

class Todo(BaseModel):
    id: Optional[int] = None
    item: str
    
    @classmethod
    def as_form(cls, item: str=Form(...), id: Optional[int] = Form(None)):
        return cls(item=item)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1"
                    },
                    {
                        "item": "Example schema 2"
                    }
                ]
            }
        }