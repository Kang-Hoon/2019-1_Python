# 스크립트 창입니다

import turtle

def draw (x,y):
    t.goto(x,y)
t = turtle.Turtle()
t.pensize(10)

s = turtle.Screen()
s.onscreenclick(draw)
