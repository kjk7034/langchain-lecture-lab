# 랭체인 입문 : 5개 프로젝트로 시작하는 LLM 기반의 AI 서비스 개발

- 패스트캠퍼스 온라인 강의
- [교육과정소개서](https://storage.googleapis.com/static.fastcampus.co.kr/prod/uploads/202309/190816-717/[%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4]-%EA%B5%90%EC%9C%A1%EA%B3%BC%EC%A0%95%EC%86%8C%EA%B0%9C%EC%84%9C-the-red---%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81,-llm-chatgpt--%EA%B8%B0%EB%B0%98%EC%9D%98-ai-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C.pdf)
- [강의 관련 자료 : github](https://github.com/jongwony/fast_campus)

## 시작하게 된 배경

최근 AI에 대한 이야기를 자주 접하면서, 나는 GPT와 Claude 같은 AI 도구들을 사용하고 있음.
하지만 사용하면서 관련 용어나 기본 지식에 대한 이해가 부족하다는 점을 느끼게 됨...

게다가, 현재 진행 중인 프로젝트에 AI를 연동할 수 있는 가능성을 보고, 사전에 필요한 기본 지식을 학습할 필요성을 절감하게 되었음.
이러한 이유로, 이번 학습을 통해 AI에 대한 기초를 다지고, 프로젝트에 효과적으로 활용할 수 있는 능력을 키우고자 신청함.

## Part 1. 기본기 돌아보기

윈도우에서 진행함.

### Python 가상 환경 설정

1. python 3.11.9 버전 설치
1. `py -m venv venv`
1. `.\venv\Scripts\activate` 가상 환경 실행. (터미널 앞에 `(venv)`가 있으면 성공)
1. `pip install ipython`으로 ipython 설치.

### 데이터 주고받는 기초

map, filter, reduce는 ES6와 다르다고 생각하지 않음.

functools는 reduce, partial ...

`partial`은 다음과 같이 사용함. (예시)

```
from functools import partial

# 두 수를 곱하는 함수 정의
def multiply(x, y):
    return (2 + x) * y

# partial을 사용해 x 값을 3으로 고정한 새로운 함수를 생성
new_function = partial(multiply, 3)

# new_function 함수를 호출하면 y 값만 필요하게 됩니다.
print(new_function(5))  # 출력: (2 + 3) * 5 = 25
print(new_function(10)) # 출력: (2 + 3) * 10 = 50
```

Itertools는 효율적인 루프를 위한 "Iterator"를 만드는 함수들. [docs python - itertools](https://docs.python.org/ko/3.11/library/itertools.html#module-itertools)참고

### 딕셔너리 쉽게 다루기

min, max, sorted, itemgetter(`__getitem__`와 같음) 등...

### JSON 쉽게 다루기

`import json`

dump, loads 등...

샘플 코드 : `json.dump(data, open('store.json', 'w'))`

JSON 데이터를 다루는 상황에서 복잡한 구조 내의 특정 데이터를 찾는 데 유용한 [jmespath](https://jmespath.org/)를 설치.(`pip install jmespath`)

```json
{
  "people": [
    { "first": "James", "last": "d" },
    { "first": "Jacob", "last": "e" },
    { "first": "Jayden", "last": "f" },
    { "missing": "different" }
  ],
  "foo": { "bar": "baz" }
}
```

```python
jmespath.search("people[*].first", people_dict)

# result : ['James', 'Jacob', 'Jayden']
```

### 매직 메서드의 이해

테스트 파일의 코드를 복사 후 붙여넣기 시 `%paste`를 입력하면 바로 반영됨. (테스트 코드 참고)

```python
# 테스트 코드
class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

classes = {
    'Point': Point
}

def serialize_instance(obj):
    """
    Point -> dict -> JSON 직렬화
    """
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


def deserialize_instance(d):
    """
    JSON -> dict -> Point 역직렬화
    """
    classname = d.pop("__classname__", None)
    if classname :
        cls = classes[classname]
        return cls(**d)
    else :
        return d


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"VectorR({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0 :
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __call__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
```

### streamit 예시 따라하기

[Streamlit API cheat sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)에 샘플 예제들을 확인함.

### 디버깅 기본

```python
# 샘플코드
def rolling_window_average(acc, new):
    window, average = acc
    window.append(new)
    if len(window) > window_size:
        window.pop(0)
    new_average = sum(window) / len(window)
    # breakpoint()
    raise
    return (window, new_average)
```

- `ipython ./part1/debug.py` 실행하면 오류를 만나면서 프로그램 종료 (raise을 추가)
- 프로그램 종료없이 계속 진행하기 위해서 i 옵션 추가해서 실행 `ipython -i ./part1/debug.py`
- 오류가 발생한 지점을 찾기 위해서 `%debug` 실행 (ipdb로 이동함.)
- `help`를 통해서 사용할 수 있는 commands 확인 (자주 사용하는 명령어)
  - p : 프린트하기
  - l(ist) : 현재 소스 코드 리스트
  - a(rgs) : 현재 함수의 인수
  - u(p) : 한 단계 위(이전 함수)
  - d(own) : 현재 스택 트레이스에서 지정된 수 만큼 (기본값은 1) 프레임을 아래로 이동
  - h(elp) : 도움말
  - q(uit) : 종료
- ipdb > `p new_average`를 실행하면 `*** NameError: name 'new_average' is not defined`가 발생함. 확인하기 위해서는 `d(down)`을 해서 다시 안으로 들어가야함.

```python
# 수정한 코드
def rolling_window_average(acc, new):
    window, average = acc
    window.append(new)
    if len(window) > window_size:
        window.pop(0)
    new_average = sum(window) / len(window)
    average.append(new_average) ## 수정 부분
    # breakpoint()
    # raise
    return (window, average)
```

위에서 테스트한 raise대신 `breakpoint()`를 사용할 수 있으며, ipdb가 아닌 pdb로 사용할 수 있으며 ipdb보다 기능은 적었다.

pdb에서 많이 사용하는 commands

- s(tep) : 함수가 있으면 첫 내부까지 실행
- n(ext) : 다음줄까지 실행
- r(eturn) : 함수 리턴까지 실행
- c(ontinue) : 다음 중단까지 실행

vscode에서 .py파일에서 파이선 실행 및 디버거 실행 기능을 활용할 수도 있다.

### Python 예외 구조

[aiohttp Hierarchy of exceptions](https://docs.aiohttp.org/en/stable/client_reference.html#hierarchy-of-exceptions)

**MRO(Method Resolution Order)**는 클래스의 메서드와 속성을 검색하는 순서 Python 클래스 계층 구조에서 중요한 역할.

### 오픈소스 Pandas 탐색하기

[Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)

#### Pandas 구성요소

- Series:
  - Dict 유사 자료구조
  - 스프레드시트에 컬럼 하나 선택한 상태와 유사
- DataFrame:
  - defaultdict(Series) 유사 자료구조
  - 스프레드시트의 시트 구조와 유사

### 오픈소스 LangChain

[python.langchain](https://python.langchain.com/v0.1/docs/get_started/introduction/)

model을 찾을 수 없다고 `model_not_found`가 계속 발생함. 원인은 Model usage에 직접 하나씩 추가해줘야 했음.

settings > Limits > Model usage에서 Allowed models 추가.

### 프롬프트 엔지니어링

[Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)

## Part 2. Streamlit을 활용한 프로젝트

### CH 1. 주식시장 분석 서비스

- 로그인 인증 관련은 구현하지 않음.
- Streamlit(프론트엔드)으로 Meilisearch, LangChain(OpenAI)을 활용해서 간단하게 기업 검색 및 분석을 구현.

#### System Prompt 정의

[Act As A Financial Analyst](https://github.com/f/awesome-chatgpt-prompts?tab=readme-ov-file#act-as-a-financial-analyst)의 내용으로 설정

영어로 작성하는게 좋은 이유 : 글자수가 한글보다 영어가 적어서 토큰 관련 비용이 절감

기대하는 정보가 나오지 않으면 `제약조건`을 추가

OpenAI 설정에서 Temperature를 0으로 적용.

Temperature를 0으로 설정하는 이유는 모델이 가능한 한 일관되고 예측 가능한 응답을 생성하도록 하기 위해서입니다. Temperature 값이 0이면 모델은 가능한 가장 가능성이 높은 답변을 선택하며, 이로 인해 답변의 다양성이 줄어들고 매우 결정론적인 응답이 생성됩니다. (gpt 답변)

meilisearch는 docker로 실행.

meilisearch에서 데이터를 최초 설정하는 과정을 bootstrap이라고 한다.

`[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:  unable to get local issuer certificate (_ssl.c:1006)')))` 같은 오류가 발생함.

fc.yahoo.com -Port 443에 접근이 가능한 것을 확인했고, `python.exe -m pip install --upgrade pip` pip upgrade하고 `pip install --upgrade certifi` certifi upgrade해서 해결함.

### CH 2. 와인정보 기반 음식 페어링 추천

- Pinecone : vector가 저장된 데이터베이스
- `pip install -r requirements.txt` 설치할 파일 모아서 한번에.
- 임베딩이란 데이터를 벡터로 변환하는 과정
- 벡터 데이터베이스를 사용하는 이유 : 계산 시스템에 최적화 되도록 데이터를 저장, 검색 (Pinecone)
- Sementic Search : 문장과 유사한 단어들을 검색
- RAG : Retrival Augmented Generation (검색엔진에서 데이터가져오기 + 증강된 데이터로 결과 생성하기)
