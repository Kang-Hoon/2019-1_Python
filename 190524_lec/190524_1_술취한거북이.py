# 스크립트 모드입니다
# 

import turtle
import random
t = turtle.Turtle()
t.shape("turtle")


for i in range(60):
    length = random.randint(1,100)
    t.forward(length)
    angle = random.randint(-180,180)
    t.rt(angle)
    
