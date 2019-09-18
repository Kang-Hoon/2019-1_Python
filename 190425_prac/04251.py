#스크립트 모드입니다.
# 연습 (1) 거북이를 불러서 육각형을 그려볼래요?

import turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()

angle = 6

t1.shape("turtle")
t2.lt(90)

i = 0

while i<angle:
    t1.fd(100)
    t1.rt(360/angle)
    i += 1

i = 0

while i<3:
    t2.fd(100)
    t2.lt(360/4)
    
input ()
