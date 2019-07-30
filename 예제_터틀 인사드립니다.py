# 스크립트 모드입니다.
#

import turtle
t = turtle.Turtle()
t.shape("turtle")
s = turtle.textinput("", "이름을 입력하시오: ")
#testinput 에 숫자를 입력해도 문자료 입력됩니다.

t.write("안녕하세요?" + s +"씨, 터틀 인사드립니다.")
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
