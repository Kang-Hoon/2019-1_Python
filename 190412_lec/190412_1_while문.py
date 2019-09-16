#스크립트 모드입니다

import turtle
t1 = turtle.Turtle()
t1.shape("turtle")

k = 1
angle = int(input("몇각형을 그리시겠어요? (3-6) : "))

print(angle,"각형을 그리겠습니다.")

while k <= angle:
    t1.fd(100)
    t1.rt(360/angle)
    k = k + 1
    
input()
