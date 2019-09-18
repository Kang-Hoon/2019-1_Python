# 스크립트 모드입니다
#

import random
import turtle

t = turtle.Turtle()

def draw_maze(x,y):
    for i in range (2):
        if i == 1 :
            t.goto (x+100, y+100)
        else:
            t.goto
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)
def turn_left():
    t.left(10)
    t.forward(10)
def turn_right():
    t.right(10)
    t.forward(10)
    t = turtle.Turtle()
    
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)

draw_maze(-300, 200)
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
t.penup()
t.goto(-300, 250)
t.speed(1)
t.pendown()

screen.listen()
screen.mainloop()
