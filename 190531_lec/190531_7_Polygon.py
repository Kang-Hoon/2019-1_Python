# 스크립트 모드입니다
#

import turtle
t = turtle.Turtle()

def poly(n,leng):
    for i in range(n):
        t.fd(leng)
        t.rt(360/n)

n = int(turtle.textinput("", "n? : "))
leng = int(turtle.textinput("", "Size of Polygon? : "))

for i in range(10):
    t.lt(20)
    poly(n,leng)
