# 스크립트 모드입니다
#

import turtle
t = turtle.Turtle()
t.shape("turtle")

s = t.textinput("", "")

if shape == "사각형":
    s = turtle.textinput("", "가로 : ")
    w = int(s)
    s = turtle.textinput("", "세로 : ")
    h = int(s)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
