# 스크립트 모드입니다.
# goto 함수 쓸거에요

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.goto(-100,300)    #좌표로 이동하는 것이에요
t.goto(-100,-300)
t.goto(0,0)

t.penup()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0,0)
t.pendown()

p = turtle.textinput("**", "숫자를 입력하세요")
n = int(p)

if (n>0):
    t.goto(100,100)
if (n==0):
    t.goto(100,0)
if (n<0) :
    t.goto(100,-100)
