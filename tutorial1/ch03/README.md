# 응답 모델과 오류 처리
- 응답 모델: api 라우트 경로가 반환하는 데이터의 템플릿 역할
    - 서버에 전달된 요청을 기준으로 적절한 응답을 렌더링하기 위해 `pydantic` 사용
## FastAPI 응답
- 응답: HTTP 메서드를 통해 API와 상호 작용하며 API로부터 받은 결과
    - json, xml 형식
    - header, body로 구성
        - header: 반환하는 콘텐츠 우형이 무엇인지 클라이언트에 알려주는 역할
            - 요청 상태 및 응답 바디 전달을 안내하는 정보로 구성.
            - ex) `Content-Type`: 반환하는 컨텐츠 유형
        - body: 서버가 클라이언트에게 반환하는 데이터
            - `Content-Type` 헤더에 의해 결정됨
            - ex)`Content-Type: application/json`
        - 상태코드: 서버가 반환한 응답에 포함되는 짧은 고유 코드. 클라이언트가 보낸 요청의 상태를 나타냄.
            - 1XX: 요청을 받음
            - 2XX: 요청을 성공적으로 처리함
            - 3XX: 요청을 리다이렉트 했음
            - 4XX: 클라이언트 측에 오류가 있음
            - 5XX: 서버 측에 오류가 있음
            > 일반적으로 프레임워크에 상관 없이 개별 요청 마다 적절한 상태코드를 반환
## 응답 모델 작성
- `pydantic`
    - 요청 모델 작성에 사용
    - `응답 모델 작성`에도 사용
    ```python
    # todo.py
    @todo_router.get("/todo", response_model=TodoItems)
    async def retrive_todo() -> dict:
        return {
            "todos": todo_list
        }
    ```
    ```python
    # model.py
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
    ```
    ### 실습
    ```shell
    uvicorn api:app --host 127.0.0.1 --port 8000 --reload
    ```
    ```shell
    # POST
    curl -X POST http://127.0.0.1:8000/todo -H "accept: applcation/json" -H "Content-Type: application/json" \
    -d '{
        "id": 1,
        "item": "This todo will be retrieved without exposing my ID!"
    }'
    ```
    ```shell
    # GET
    curl -X GET http://127.0.0.1:8000/todo -H "accept: applcation/json"
    ```

## 오류 처리
- 존재하지 않는 리소스나 권한이 없는 페이지에 접근하는 요청의 경우 오류가 발생
- 이를 예외 처리: `HTTPException`는 3개의 인수를 받는다.
    - `status_code`: 예외 처리 시 반환할 상태 코드
    - `detail`: 클라이언트에게 전달한 메시지
    - `headers`: 헤더를 요구하는 응답을 위한 선택적 인수

    ```python
    @todo_router.put('/todo/{todo_id}')
    async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
        for todo in todo_list:
            if todo.id == todo_id:
                todo.item = todo_data.item
                return {
                    "message": "Todo updated successfully."
                }
        # 페이지가 없을 경우 예외 처리
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist."
        )
    ```

    ```python
    @todo_router.post('/todo', status_code=201) # status_code: 기본 응답 코드도 변경 가능
    async def add_todo(todo: Todo) -> dict:
        todo_list.append(todo)
        return {
            "message": "Todo item added successfully."
        }
    ```