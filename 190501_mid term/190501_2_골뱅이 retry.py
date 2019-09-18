# 스크립트 모드입니다
# 골뱅이를 그려봅시다

import turtle

t = turtle.Turtle()
t.shape("turtle")
turtle.bgcolor("black")
color = ["red", "blue", "green", "pink", "yellow", "white"]

t.width(2)
t.speed(100)
length = 10

while length<500:
    t.fd(length)
    t.pencolor(color[length%6])
    t.rt(89)
    length += 1

# 완벽하게 이해했나?
