# 템플릿팅
- API가 보낸 다양한 형식의 데이터를 화면에 표시하는 프로세스
- 웹 애플리케이션상의 프론트엔드 컴포넌트 처럼 처리됨

## Jinja
- 파이썬으로 작성된 템플릿팅 엔진
- API 응답을 쉽게 렌더링할 수 있도록 함
- 문자열로 변환 가능한 모든 파이썬 유형 또는 객체를 템플릿 변수로 사용할 수 있음
### 구문
- `{% ... %}`: 구조(처리)를 제어하기 위한 명령을 지정
- `{{todo.item}}`: 식의 값을 전달할 때 사용. 모델, 리스트, 딕셔녀리 유형을 템플릿에 전달해서 값이나 속성을 사용 가능
- `{# 이책은 훌륭한 API 책이다. #}`: 주석 기입
### 필터
- `|`: 변수와 구분하여 괄호를 사용해 선택적 인수를 지정. 수정 작업에 사용
    - ex) 인수가 있는 경우: `{{ variable | filter_name(*args) }}`
    - ex) 인수가 없는 경우: `{{ variable | filter_name }}`
    #### 기본 필터
    - 전달된 값이 `None`일 때, 사용할 값을 지정
    - `{{ todo.item | default('이것은 기본 todo 아이템 잆니다.')}}`
    #### 이스케이프 필터
    - HTML을 변환하지 않고 그대로 렌더링
    - `{{ "<title>Todo Application</title>" | escape}}`
        - 결과: `<title>Todo Application</title>`
    #### 변환 필터
    - 데이터 타입을 변환
    - `{{ 3.142 | int }}`
        - 결과: 3
    #### 병합 필터
    - 리스트 내의 요소들을 병합해서 하나의 문자열로 만든다.
    - `{{ ['aa', 'bbb']}}`
        - 결과: aabbb
### if
- 파이썬 방법과 유사

    ```
    {% if todo | length < 5 %}
        blah..

    {% else %}
        blah2..

    {% endif %}
    ```
### 반복문
- 파이썬 방법과 유사

    ```
    {% for todo in todos %}
        <b>{{ todo.item }}</b>
    {% endfor %}
    ```

- 반복문에서 사용되는 특수 변수

    |변수|설명|
    |---|---|
    |index|반복의 현재 인덱스(회차)를 보여줌(시작 인덱스는 1)|
    |index0|반복의 현재 인덱스를 보여줌(시작 인덱스는 0)|
    |revindex|뒤에서부터의 반복 인덱스를 보여줌(시작 인덱스는 1)|
    |revindex0|뒤에서부터의 반복 인덱스를 보여줌(시작 인덱스는 0)|
    |first|첫 번째 반복이면 True를 반환|
    |last|마지막 반복이면 True를 반환|
    |length|리스트 등의 아이템 수를 반환|
    |cycle|리스트 내의 값을 차례대로 사용|
    |depth|재귀적 반복에서 현재 렌더링 단계를 보여줌(1단계부터 시작)|
    |depth0|재귀적 반복에서 현재 렌더링 단계를 보여줌(0단계부터 시작)|
    |previtem|이전 반복에 사용한 아이템을 반환(첫 반복에서는 정의되지 않음)|
    |nextitem|다음 반복에 사용할 아이템을 반환(마지막 반복에서는 정의되지 않음)|
    |changed(*val)|이전에 호출한 값과 다르다면 True 반환(전혀 호출되지 않은 경우도 포함)|

### 매크로
- 하나의 함수. HTML 문자열을 반환
- 매크로 사용의 주요 목적은 하나의 함수를 사용해 반복적으로 작성하는 코드를 줄이는 것
    - 아래 매크로를 호출해서 폼에 사용할 입력 요소를 간단하게 만들 수 있다.

        ```jinja
        {% macro input(name, value='', type='text', size=20) %}
            <div class="form">
                <input type="{{ type }}" name="{{ name }}" value="{{ value | escape }}" size="{{ size }}">
            </div>
        {% endmacro %}
        ```
    - 아래 매크로는
        ```jinja
        {{ input('item') }}
        ```
    - 다음과 같은 HTML을 반환한다.
        ```html
        <div class="form">
            <input type="text" name="item" value="" size="20">
        </div>
        ```
### 템플릿 상속
- DRY 원칙에 근거한 가장 강력한 기능
- 자세히 알고 싶으면 https://jinja.palletsprojects.com/en/3.0.x/templates/#template-inheritance

## FastAPI에서 템플릿팅을 사용하는 방법
1. Jinja2 패키지 설치
2. 기존 작업 디렉토리에 `template` 신규 폴더 생성
> 본 책은 UI 디자인을 다루지 않으므로 CSS 부트스트랩 라이브러리를 사용한다.

### setting
- `run.sh` 참고

