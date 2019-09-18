# 스크립트 모드입니다
#

import turtle
t = turtle.Turtle()

def square(len):
    for i in range(4):
        t.fd(len)
        t.rt(90)

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color("yellow")
    square(50)
    t.end_fill()

s = turtle.Screen()      #그림이 그려지는 캔버스르 생성
s.onscreenclick(drawit)  #마우스 클릭 이벤트 처리 함수를 등록

# drawit (0,0)
