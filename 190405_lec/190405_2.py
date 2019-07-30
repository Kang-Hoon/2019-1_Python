#스크립트 모드
#집그리기

import turtle
turtle.Turtle()

t1 = turtle
t1.shape("turtle")

size = int(input("집의 크기는 몇 픽셀로 할까? "))
angle = 90

t1.fd(size)
t1.rt(angle)
t1.fd(size)
t1.rt(angle)
t1.fd(size)
t1.rt(angle)
t1.fd(size)

t1.rt(30)
t1.fd(size)
t1.rt(120)
t1.fd(size)

