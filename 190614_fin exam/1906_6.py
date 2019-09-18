# 스크립트 창입니다

import random

time = random.randint(1,24)

print("Hello, it's %s ." %time)

sunny = random.choice([True, False])

if sunny :
    print("IT'S SUNNY DAY")
else :
    print("IT IS NOT")

if time<9 and time>=6 and sunny:
    print("Bird sings")
else :
    print("Bird do tnot sing")
