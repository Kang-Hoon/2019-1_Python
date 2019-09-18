# 스크립트 모드입니다
# 거북이를 제어하자

import turtle

t = turtle.Turtle()
t.shape("turtle")

# 거북이를 3배 확대한다
t.shapesize(3,3)

t.width(3) #거북이는 키워놓고 선은 안 키울거야?

while True:
    command = input("명령을 입력하시오 : ")

    if command == "l":
        t.left(90)
        t.forward(100)
    if command == "r":
        t.right(90)
        t.forward(100)
    if command == "f":
        t.left(360)
        t.forward(100)
    if command == "x":
        break
