# 스크립트 창입니다

import turtle

def draw(height):
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.write(str(height), font = ('Calibri', 16, 'bold'))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

data = [120, 56, 309, 220, 156, 23, 98]

t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")

t.pensize(3)

for d in data:
    draw(d)

t.hideturtle()
