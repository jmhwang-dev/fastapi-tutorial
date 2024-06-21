import asyncio
import pytest

from database.connection import Settings
import httpx

from main import app
from models.events import Event
from models.users import User

# 활성 루프 세션을 만들어서 테스트가 단일 스레드로 실행되도록 함
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"     # 새로운 데이터베이스 인스턴스 생성: testdb
    await test_settings.initialize_database()

@pytest.fixture(scope="module")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client

        # 리소스 정리
        await Event.find_all().delete()
        await User.find_all().delete()
