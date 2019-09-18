
# 스크립트 모드입니다
# 흰색 거북이가 검은색 바다를 원을 그리며 헤엄칠 예정입니다

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("white")

turtle.bgcolor("black")

box = int(turtle.textinput("창이름", "뭐야"))

t.circle(box)
