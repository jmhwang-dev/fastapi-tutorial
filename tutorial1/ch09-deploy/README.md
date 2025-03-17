# 9.1 배포 준비
## 의존 라이브러리 관리
- 주요 라이브러리만 추출해서 작성한다.
```sh
pip freezie > requirements.txt
```

## 환경변수 설정
- 버전 관리 시스템에서는 제외시키는 것이 좋다.

# 9.2 도커
## `Dockerfile` 작성
```bash
touch Dockerfile
```

```Docker
# Dockerfile

## 기본 이미지 지정
FROM python:3.12

## 도커 내 작업 디렉토리 설정: 작업 디렉토리는 이미지로 빌드될 프로젝트 구조를 정리할 때 도움이 된다.
WORKDIR /app

## 로컬 디렉토리에서 `requirement.txt`를 도커 컨테이너의 작업 디렉토리로 복사한다.
COPY requirements.txt /app/requirements.txt

## 도커 내 에서 의존 라이브러릴 설치한다.
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

## 로컬 네트워크에서 애플리케이션에 접속할 수 있는 포트 번호를 설정한다.
EXPOSE 8000

## 나머지 파일을 도커 컨테이너의 작어 디렉토리로 복사한다.
COPY ./ /app/

## 애플리케이션을 실행한다.
CMD ["python", "main.py"]
```
- 도커파일의 각 명령은 개별 레이어로 빌드된다.
- 도커는 각 레이어에 캐시를 적용해서 빌드 시간을 줄이고 반복을 제거한다.

## `.dockerignore` 작성
```docker
# Dockerfile에 정의된 명령을 실행할 때 제외할 파일 폴더 지정 
.fastapi
.env
.git
```

## docekr image build
- 도커 빌드
```bash
docker build -t event-planner-api .
```

- 빌드 후 이미지 생성 확인
```bash
docker image ls --filter reference=event-planner-api
```

## MongoDB image pull
- API 컨테이너가 접근할 수 있는 데이터베이스 컨테이너 생성
```
docker pull mongo
```

# 로컬에 애플리케이션 배포
- 도커 구성 파일 작성
```bash
touch docker-compose.yml
```

```docker
version: '3'    # 더 이상 사용 안함

services:
  api:
    build: .    # 현재 디렉터리에 있는 도커파일을 기준으로 `event-planner-api:latest` 이미지를 빌드한다.
    image: event-planner-api:latest # 8000번 포트를 노출해서 http를 통해 API에 접근하도록 한다.
    ports:
      - "8000:8000"
    env_file:
      - .env.prod   # `.env.prod` 파일을 환경 파일로 설정한다.
  database:
    image: mongo:latest # 앞서 pull한 이미지를 사용한다.
    ports:
      - "27017"     # 포트를 정의했으나 외부로 노출하진 않는다. 위에서 정의한 `api` service만 이 포트에 접근할 수 있다.
    volumes:
      - data:/data/db   # 영구적 볼륨(저장소)을 서비스에 할당해서 데이터를 저장하는데 사용한다. 여기서는 /data/db 폴더가 사용된다.

volumes:
  data: # `data`라는 볼륨을 할당하여 배포에 사용한다.
```

## .env.prod 대신 아래 내용으로 `docker-compose.yml`에 구성할 수 있다.
```docker
enviroment:
    - DATABSE_URL=mongodb://database:27017/planner
    - SECRET_KEY=secretkey
```
