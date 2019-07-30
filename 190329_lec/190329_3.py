
# 스크립트 모드입니다

import turtle
t1=turtle.Turtle('triangle')
t2=turtle.Turtle('turtle')

colors = ["red", "blue", "green"]
turtle.bgcolor("yellow")
t1.speed(10)
t1.width(5)
length1 = 10

t2.speed(8)
t2.width(5)
t2.pencolor('pink')
length2 = 10

while length1 < 600:
    t1.fd(length1)
    t1.pencolor(colors[length1%3])
    t1.right (89)
    length1 += 3 #length1 = length1 + 3
while length2 < 600:
    t2.fd(length2)
    t2.pencolor('blue')
    t2.left (88)
    length2 += 4 #length2 = length2 + 4

input()
