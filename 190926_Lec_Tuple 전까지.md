# 190926 Python LEC

### 파이썬 자료구조 (data structure)

​	리스트	하나의 변수에 여러 값을  할당 관리하는 자료구조

​	튜플		데이터 변경 허용 X

​	세트		데이터 중복 허용 X, 수학의 집합 연산을 지원하는 자료 구조

​	딕셔너리 key와 value 형태의 데이터를 저장하는 자료구조 (키값 중복 허용 					X)

#### 시퀀스

* 요소로 구성, 요소 간에 순서가 있다

* 시퀀스 요소들은 번호를 부여, 인덱스는 0번부터 부여

* 시퀀스에 속하는 자료구조들은 동일한 연산을 지원

* ```python
  >>> n = [10, 20, 30, 40, 50]
  >>> id(n)
  4324685512
  >>> id(n[0])
  4306922960
  >>> id(n[1])
  4306923280
  >>> id(10)
  4306922960
  >>> id(20)
  4306923280
  ```

  

#### 리스트

* 문법 ex (in, not in, len())

```python
>>> n = [10, 20, 30, 40, 50]
>>> n.append(60)
>>> n
[10, 20, 30, 40, 50, 60]
>>> n.clear()
>>> n
[]
>>> n.append(200)
>>> n
[200]
```

![page24image7051152.png](/Users/yongmin/Library/Application Support/typora-user-images/page24image7051152.png) 

₩예제)

```python
print("다음 실행결과 중 원래의 값에 영향을 주지 않는 것을 모두 고르시오")
```

₩insert() 예시     <insert(인덱스, 데이터)>

```python
>>> n = []
>>> n.append(10)
>>> n
[10]
>>> n.append(20)
>>> n
[10, 20]
>>> n.append(30)
>>> m
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    m
NameError: name 'm' is not defined
>>> n
[10, 20, 30]
>>> n.insert(10)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    n.insert(10)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> n.insert(1,15)
>>> n
[10, 15, 20, 30]
```



//  is 로 리스트의 데이터 값을 물어보는 것은 데이터의 메모리의 위치를 물어보는 것이다.

'is' != '=='







