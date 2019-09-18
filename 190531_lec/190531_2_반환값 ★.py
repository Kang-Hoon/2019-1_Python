# 스크립트 모드입니다
#

def add ():                 # 함수 정의
    print("대전광역시 유성구")
    print("지족동")

add()                       # 함수 호출
add()

def add1 (name):
    print(name)

def add2 (name, addr):
    print(name)
    print(addr)

add2("이강훈", "죽전동")        # 함수 호출

    # 이 예제에서는 add2 함수만 사용하기 때문에 add1 함수 내에
    # 오타가 생기더라도 파일을 실행시키는데 오류가 생기지 않는다.
