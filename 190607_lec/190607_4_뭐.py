# 스크립트 모드입니다
#

import turtle

def draw(x,y):
    t.goto(x,y)

def circle():
    t.circle(50)

def square():
    for i in range(4):
        t.fd(100)
        t.lt(90)

t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)

s = turtle.Screen()
s.onscreenclick(draw)       # 마우스 클릭 이벤트 처리 함수를 등록한다

s.onkey(t.penup, "Up")      # 키보드 이벤트 처리 함수를 등록한다
s.onkey(t.pendown, "Down")  # 키보드 이벤트 처리 함수를 등록한다
s.onkey(circle, "1")
s.onkey(square, "2")        

s.listen()                  # 키보드 이벤트를 기다린다
