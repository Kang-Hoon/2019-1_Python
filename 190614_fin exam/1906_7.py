# 스크립트 창입니다

import random

dirgol = random.choice(["left","center","right"])
d = str(input("What's Direction? (left/center/right) "))

if dirgol==d :
    print ("You failed ")
else :
    print(" Scored! ") 
