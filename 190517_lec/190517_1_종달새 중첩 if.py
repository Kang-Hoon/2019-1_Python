# 스크립트 모드입니다
#

import random

time = random.randint(1,24)
print("Good Morning, Sir! It's " + str(time) + "'O clock!")

sunny = random.choice([True, False])

if sunny:
    print("It's such a good day")
else:
    print("It's such a gloomy day")

if time >= 6 and time <9 and sunny:
    print("A bird is singing")
else:
    print("The bird is gone")
