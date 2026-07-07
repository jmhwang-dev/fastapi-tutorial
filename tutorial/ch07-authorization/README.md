# 7.1 FstAPI 인증 방식
### 기본 HTTP 인증
- 사용자명, 패스워드를 `Authorization HTTP` 헤더를 사용해 전송하는 방식
#### 반환 값
- `Basic` 값을 포함하는 `WWW-Authenticate` 헤더
- 인증 요청을 처리한 리소스를 나타내는 `realm` 매겨변수가 반환된다.

### 쿠키
- 데이터를 클라이언트 측에 저장할 때 사용
- 서버는 이 정보를 추출해 인증 처리에 사용

### bearer 토큰 인증 - JWT
- `bearer`토큰 이라는 보안 토큰을 사용해 인증하는 방식
- 이 토큰은 `Bearer` 키워드와 함께 요청의 `Authorization` 헤더에 포함돼 전송된다.`
#### 구성
- 딕셔너리 형식이 일반적이며 아래 항목들로 구성된다.
    - 사용자 ID
    - 토큰 만료 기간으로 구성
---
- 위 방법들은 모두 장단점이 있으며 사용되는 곳도 다르다.
- 여기서는 `bear` 토큰 인증을 사용한다.
- 인증에 사용되는 메서드는 런타임 시 호출되는 의존 라이브러리로 FastAPI 애플리케이션에 주입된다.

## 의존성 주입
- 한 객체가 사용할 객체를 직접 생성하지 않고, 외부에서 주입받는 디자인 패턴
- FastAPI에서는 라우트 처리 함수의 인수로 의존 라이브러리를 주입한다.

```python
# ch06에서 이미 의존성 주입을 사용했다.
@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    """
    의존 라이브러리느 User class. `sign_user_up()`에 주입한다.
    """
    user_exist = await User.find_one(User.email == user.email)
```

## 의존 라이브러리 생성
- `FastAPI`에서 의존 라이브러리는 함수 또는 클래스로 정의된다.
```python
# 의존 라이브러리 예시
async def get_user(token: str):
    user = decode_token(token)
    return user
```
- 위 라이브러리를 사용하려면 `Depends` 매개변수를 사용하고자 하는 함수의 인수로 설정해야한다.
```python
from fastapi import Depends

@router.get("/user/me")
async get_user_details(user: User = Depends(get_user)):
    return user
```

# 7.2 OAuth2와 JWT를 사용한 애플리케이션 보안
## 인증 방식
- `Form` 데이터가 클라언트에서 서버로 전송되면 서버는 `JWT`로 로그인 된 액세스 토큰을 응답으로 반환한다.

### OAuth2
- OAuth 2.0은 웹 애플리케이션, 데스크톱 애플리케이션, 모바일 애플리케이션 및 기타 장치에서 리소스(예: 사용자 데이터)에 액세스하기 위해 널리 사용되는 인증 프레임워크
- OAuth 2.0은 클라이언트가 자원을 소유한 사용자의 권한을 얻고, 그 권한을 기반으로 보호된 리소스에 접근할 수 있도록 한다.

### Json Web Token
- JSON 객체를 사용하여 클레임(claim)을 안전하게 전달하기 위한 컴팩트하고 자가 포함된 방식
- 서버와 클라이언트만 알고 있는 고유한 키로 사인된다.
- 주로 인증 및 정보 교환에 사용된다.

#### 구조
- 인코딩된 문자열로 다음으로 구성된다.
    - Payload
    - Signiture
    - Algorithm

# 7.3 실습
- 코드 참조

# 7.4 CORS 설정
- 등록되지 않은 사용자가 리소스를 사용하지 못하도록 제한하는 규칙
- 프론트엔드 애플리케이션이 web API를 호출하면 브라우저가 호출의 출처를 확인해서 제한한다.
- `CORSMiddleware`라는 미들웨어를 통해 API 접근 가능한 출처를 관리한다.
> 미들웨어: 하나의 함수로, 특정 처리 사이의 중개자 역할을 한다. Web API에서 미들웨어는 요청과 응답 간 중개자이다.
```python
# main.py
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]     # 모든 클라이언트의 요청을 허가. `*`는 와일드카드를 의미하며, API에거 모든 요청을 허가하도록 지시한다
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```