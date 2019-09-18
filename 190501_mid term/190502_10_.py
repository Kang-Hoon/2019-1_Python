# 스크립트 모드입니다
# turtle

import turtle
t1.turtle.Turtle()
t1.shape("turtle")

d = 100
ang = 90

s = turtle.inputtext("", "이름이 뭐에요?")
t1.write("안녕하세요", s, "씨, 터틀 인사드려요~")

i = 1               #start
while i <= 4 :      #stop
    t1.fd(d)
    t1.lt(ang)
    i = i + 1       #step
