# 스크립트 모드입니다
#

def cal(rad):
    area = 3.14 * rad**2
    return area

n = int(input("원의 넓이 반지름 : "))
c = cal(n)
print("반지름 %s 의 원의 넓이는 %s 이다" %(n,c))
