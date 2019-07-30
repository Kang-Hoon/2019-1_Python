#190405 파이썬 수업 1
#스크립트 모드_변수를 이용한 원 그리기

import turtle
t1 = turtle.Turtle()
t1.shape("turtle")

radius = 50
t1.circle(radius) #반지름이 50인 원이 그려진다.
t1.fd(50)
t1.circle(radius) 
t1.fd(50)
t1.circle(radius) 
t1.fd(50)
t1.circle(radius) 

t1.rt(90)
t1.fd(200)
t1.rt(90)

fdval = 50
t1.circle(radius) #반지름이 50인 원이 그려진다.
t1.fd(fdval)
t1.circle(radius) 
t1.fd(fdval)
t1.circle(radius) 
t1.fd(fdval)
t1.circle(radius) 
