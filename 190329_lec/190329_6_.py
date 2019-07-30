
# 스크립트 모드입니다

import turtle
t1=turtle.Turtle('triangle')
t2=turtle.Turtle('turtle')

colors = ["red", "blue", "green"]
turtle.bgcolor("black")
t1.speed(0)
t1.width(3)
length1 = 10

t2.speed(0)
t2.width(3)
t2.pencolor('pink')
length2 = 10

while length1 < 600:
    t1.fd(length1)
    t1.pencolor('pink')
    t1.right (80)
    length1 += 3 #length1 = length1 + 3
while length2 < 600:
    t2.fd(length2)
    t2.pencolor('pink')
    t2.left (82)
    length2 += 4 #length2 = length2 + 4
input()
