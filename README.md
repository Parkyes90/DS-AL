# 자료구조

## 추상 데이터 타입 (Abstract Data Type)

ADT는 유사한 동작을 가진 자료구조의 클래스에 대한 수학적 모델을 가리킨다.


### 스택

배열의 끝에서만 데이터 접근 가능한 선형 자료구조

#### 기능
```
push : 스택 맨 끝에 항목 삽입
pop : 스택 맨 끝 항목 반환 & 제거
top/peek : 스택 맨 끝 항목 조회
is_empty : 스택이 비어있는지 확인
size : 스택 크기 확인
```

### 큐

먼저 들어온 데이터가 먼저 나가는 선입선출 구조

#### 기능
``` 
enqueue : 큐 뒤쪽에 항목 삽입
dequeue : 큐 앞쪽의 항목 반환 & 제거
peek/front : 큐 앞쪽 항목 조회
is_empty : 큐가 비어있는지 확인
size : 큐의 크기 확인
```

### Deque

양쪽 끝에서 항목의 조회, 삽입, 삭제 가능

#### 기능
``` 
enqueue : 큐 뒤쪽에 항목 삽입
dequeue : 큐 앞쪽의 항목 반환 & 제거
peek/front : 큐 앞쪽 항목 조회
is_empty : 큐가 비어있는지 확인
size : 큐의 크기 확인
enqueue_back : 큐 앞 쪽에서 항목 삽입
dequeue_front : 큐 뒤쪽의 큐 반환 & 제거
```
