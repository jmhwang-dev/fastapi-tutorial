from fastapi import FastAPI

app = FastAPI() # 라우트 생성

@app.get("/")   # 처리 유형 정의
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }