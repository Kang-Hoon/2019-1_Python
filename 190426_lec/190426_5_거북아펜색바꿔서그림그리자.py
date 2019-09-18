# 스크립트 모드입니다.
# 거북아 원을 채우자
# 거북아 펜 색을 바꾸자

import turtle
t1 = turtle.Turtle()
t1.shape("turtle")

color_list = ["yellow", "red", "blue", "Pink", "green", "" ]
pencolor_list = ["brown", "yellow", "red", "blue", "Pink", "green" ]

n = 0
for n in range(5):
    t1.fillcolor(color_list[n])
    t1.pencolor(pencolor_list[n])
    t1.begin_fill()
    t1.circle(100)
    t1.end_fill()
    t1.up()
    t1.fd(100)
    t1.down()

# for i in color_list:
#   t.fillcolor(i)

# for i in ["yellow", "red", "blue", "green"]:
#   t.fillcolor(i)

# for i in range(0,4,1):
#   t.fillcolor(color_list[i])

# for i in range(4):
#   t.fillcolor(color_list[i])

# for i in [0,1,2,3]
#   t.fillcolor(color_list[i])
