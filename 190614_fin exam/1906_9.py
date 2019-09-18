# 스크립트 창입니다

import turtle
import random

t = turtle.Turtle()


t.shape("turtle")
a = int(turtle.textinput("",""))
for i in range (a):
    length = random.randint(1,100)
    t.fd(length)
    angle = random.randint(-180, 180)
    t.rt(angle)
