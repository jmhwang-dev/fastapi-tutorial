from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import Settings
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    await settings.initialize_database()
    yield
    

app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix='/user')
app.include_router(event_router, prefix='/event')

# 출처 등록
origins = ["*"]     # 모든 클라이언트의 요청을 허가. `*`는 와일드카드를 의미하며, API에거 모든 요청을 허가하도록 지시한다
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)