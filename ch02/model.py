# 파이썬의 타입 어노테이션을 사용해서 데이터를 검증하는 파이썬 라이브러리
from pydantic import BaseModel

class Item(BaseModel):
    item: str
    status: str
class Todo(BaseModel):
    id: int
    item: str

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
                "item": "Read teh next chapter of the book"
            }
        }