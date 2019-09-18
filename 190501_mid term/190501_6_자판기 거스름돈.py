# 스크립트 모드입니다
# 거스름돈 계산하는 프로그램을 만들거에요

income = int(input("투입한 돈은 얼마입니까? : "))
price = int(input("물건의 값은 얼마입니까? : "))
change = income - price

c500 = change // 500
print(c500)
change = change % 500

c100 = change // 100
print(c100)
change = change % 100

c50 = change // 50
print(c50)
change = change % 50

c10 = change // 10
print(c10)

# 내맘같지 않네...
