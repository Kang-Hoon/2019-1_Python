# 스크립트 모드입니다
#

option = ["Left", "Center", "Right"]
choice_comp = random.choice(option)
choice_user = input("What is your choice? (Left, Center, Right) ")

if choice_comp == choice_user:
    print("Computer won!")
else:
    print("You won!")
