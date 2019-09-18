# 스크립트 창입니다

import turtle

t = turtle.Turtle()

t.penup()
t.goto(100,100)
t.write("It's positive integer")
t.goto(100,0)
t.write("It's Zero")
t.goto(100,-100)
t.write("It's negative integer")
t.goto(0,0)
t.pendown()

i = turtle.textinput("","Enter integer : ")
j = int(i)

if j>0:
    t.goto(100,100)
if (j==0):
    t.goto(100,0)
if j<0:
    t.goto(100,-100)
