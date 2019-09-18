# 스크립트 모드입니다
#

import turtle
t = turtle.Turtle()

def square(len):
    for i in range(4):
        t.fd(len)
        t.rt(90)

n = int(input("Size of Square : "))

for i in range(3):
    square(n)
    t.up()
    t.fd(100)
    t.down()
