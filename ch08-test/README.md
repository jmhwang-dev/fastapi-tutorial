# 8.1 `pytest`를 사용한 단위 테스트
```
pip install pytest
```
> `test_arithmetic_operation.py` 참조

## 픽스쳐를 사용한 반복 제거
- `fixture`: 재사용할 수 있는 함수로, 테스트 함수에 필요한 데이터를 반환하기 위해 정의된다.

```python
import pytest
from models.events import EventUpdate

# 픽스쳐 정의
@pytest.fixture
def event() -> EventUpdate:
    """
    - EventUpdate pydantic 모델의 인스턴스를 반환하는 픽스쳐를 정의한다.
    - 이 픽스쳐는 `test_event_name()`의 인수로 사용된다.
    """
    return EventUpdate(
        title = "FastAPI Book Launch CLI",
        image = "https://linktomyimage.com/image.png",
        description = "열심히 열심히",
        tags = ["python", "fastapi", "book", "launch"],
        location = "Google Meet'
    )
```
```python
def test_event_name(event: EventUpdate) -> None:
    assert event.title == "FastAPI Book Launch CLI"
```