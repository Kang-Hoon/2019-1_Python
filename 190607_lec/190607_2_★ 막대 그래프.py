# 스크립트 모드입니다
#

import turtle

t = turtle.Turtle()

def drawBar (height):
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.write(str(height), font = ('', 16))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

data = [120, 56, 309, 220, 156, 23, 98]

t.color("blue")
t.fillcolor("red")

t.pensize(5)

for d in data:
    drawbar(d)

t.hideturtle()
