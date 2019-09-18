# 스크립트 모드입니다
#

import random

print("동전 뒤집기 게임을 시작하지 ")

coin = random.randrange(2)

if coin == 0 :
    print("앞면입니다")
else :
    print("뒷면입니다")

print("게임이 끝났다.")
