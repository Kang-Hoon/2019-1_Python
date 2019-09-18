import turtle
import random

t = turtle.Turtle()

t.pensize(1)
t.speed(0)

# 0.좌표

# 1.축구장을 그립니다.
def stad():
    t.up()
    t.goto(-200,200)
    t.down()
    t.pensize(5)
    t.fd(300)
    t.rt(90)
    t.fd(450)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(450)
    t.rt(90)

# 2.벤치를 그립니다.
def benc():
    t.up()
    t.goto(100,50)
    t.down()
    t.fd(50)
    t.rt(90)
    t.fd(150)
    t.rt(90)
    t.fd(50)
    t.up()
    t.goto(150,-25)
    t.down()
    t.fd(350)

# 3.센터서클을 그립니다.
def cent():
    t.up()
    t.goto(-100,-25)
    t.down()
    t.lt(90)
    t.circle(50)

# 4.1 포메이션 4-4-2
# 4.2 포메이션 4-1-2-1-2

stad()
benc()
cent()

# turtle.textinput("", "")

listA = []
listB = []
listC = []
listD = []

lena = len(listA)
lenb = len(listB)
lenc = len(listC)
lend = len(listD)

for i in range(2):
    listA.append(turtle.textinput("","공격수"))
for i in range(4):
    listB.append(turtle.textinput("","미드필더"))
for i in range(4):
    listC.append(turtle.textinput("","수비수"))
for i in range(1):
    listA.append(turtle.textinput("","골키퍼"))

numa = random.randint(0,len(listA))

t.up()
t.goto(-100,150)
t.down()
for ah in range(-100, 50, 2):
             t.write(listA[a])
print()

t.up()
t.goto(-180,50)
t.down()
for b in range(4):
             t.write(listB[b], end=' ')
print()

t.up()
t.goto(-180,-100)
t.down()
for c in range(4):
             t.write(listC[c], end=' ')
print()

t.up()
t.goto(-60,-250)
t.down()
print(listD)
print()

#
#i = 0
#for i in range(4):
#    listA.append(i)
#    t.write(list[i])
#j = 0
#for j in range(4):
#    listB.append(j)
#    
#k = 0
#for k in range(4):
#    listC.append(k)
#
#l = 0
#for l in range(4):
#    listD.append(l)

