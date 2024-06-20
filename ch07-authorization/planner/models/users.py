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
            }
        }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str