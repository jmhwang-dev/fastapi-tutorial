from pydantic import EmailStr
from typing import Optional, List
from models.events import Event
from beanie import Document
from pydantic import BaseModel

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str