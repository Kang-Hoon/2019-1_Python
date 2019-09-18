# 스크립트 모드입니다
#

total = 0
answer = "yes"
while answer == "yes":
    number = int(input("Enter integer number : "))
    total = total + number
    answer = input("Continue? (yes or no)")
print("Total sum is ", total)
