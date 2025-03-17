from beanie import init_beanie, PydanticObjectId
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Optional, Any, List
from motor.motor_asyncio import AsyncIOMotorClient

from models.events import Event
from models.users import User
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, model) -> None:
        self.model = model

    # 생성 처리
    async def save(self, document) -> None:
        await document.create()
        return
    
    # 조회 처리
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self,) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    # 변경 처리
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc = await self.get(id)
        if not doc:
            return False
        
        des_body = body.model_dump()
        des_body = {k: v for k, v in des_body.items() if v is not None}

        update_query = {
            "$set": {
                field: value for field, value in des_body.items()
            }
        }

        await doc.update(update_query)
        return doc
    
    # 삭제 처리
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Event, User])

    class Config:
        env_file = ".env.prod"