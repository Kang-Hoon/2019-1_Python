# 스크립트 모드입니다
#

import turtle
t = turtle.Turtle()

def tree(length):
    if length>5:
        t.fd(length)
        t.right(20)
        tree(length-15)
        t.lt(40)
        tree(length-15)
        t.rt(20)
        t.backward(length)

t.lt(90)

t.color("green")
t.speed()
tree(90)
