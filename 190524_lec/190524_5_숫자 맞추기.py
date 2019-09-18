# 스크립트 모드입니다
#

import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("Get answer from 1 to 100 ")

while guess != answer:
    guess = int(input("숫자를 입력하세요 : "))
    tries = tries + 1
    if guess<answer :
        print("↑")
    elif guess>answer :
        print("↓")
if guess == answer :
    print("Congratulation!")
