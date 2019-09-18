# 스크립트 모드입니다.
# 거북아 원을 채우자

import turtle
t1 = turtle.Turtle()
t1.shape("turtle")

color_list = ["yellow", "red", "blue", "Pink", "green", "" ]

n = 0
for n in range(4):
    t1.fillcolor(color_list[n])
    t1.begin_fill()
    t1.circle(100)
    t1.end_fill()
    t1.fd(100)



