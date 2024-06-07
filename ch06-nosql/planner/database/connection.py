from beanie import init_beanie
from pydantic import BaseSettings
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient

from models.events import Event
from models.users import User

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Event, User])

    class Config:
        env_file = ".env"