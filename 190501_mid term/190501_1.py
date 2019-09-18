#스크립트 모드입니다
#골뱅이를 그려봅시다

import turtle
t = turtle.Turtle()
t.shape("turtle")
turtle.bgcolor("black")

color = ["red", "blue", "green", "pink", "yellow"]

t.speed(100)
t.width(4)

length = 10

while length<500:
    t.fd(length)
    t.pencolor(color[length%5])
    t.rt(89)
    length += 1

# not bad
