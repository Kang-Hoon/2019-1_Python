# 스크립트 모드입니다
# 터틀로 인풋텍스트로 크기를 받아 집을 그립시다

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("white")
turtle.bgcolor("black")

s = turtle.inputtext("집 크기좀 보자", "집의 크기는 얼마인가요? (20~200) : ")

t.fd(s)
t.lt(120)
t.fd(s)
t.lt(120)
t.fd(s)
t.lt(30)

t.fd(s)
t.lt(90)
t.fd(s)
t.lt(90)
t.fd(s)

# 이건 어떤가
