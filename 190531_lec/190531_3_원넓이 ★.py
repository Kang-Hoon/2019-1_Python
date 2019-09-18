# 스크립트 모드입니다
#

def cal(rad):
    area = 3.14 * rad**2
    return area

cal(10)

print (cal(10))

# without 'return area'
def cal(rad):
    area = 3.14 * rad**2

#   return area

cal(10)

print (cal(10))
