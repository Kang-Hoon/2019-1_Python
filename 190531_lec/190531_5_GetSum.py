# 스크립트 모드입니다
#

def get_sum(start, end):
    total = 0
    for i in range(start, end+1):
        total = total + i
    return total

s = int(input("시작값 :"))
e = int(input("끝 값 :"))
