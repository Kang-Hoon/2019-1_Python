#스크립트 모드입니다
#자판기 프로그램

moneyin = int(input("얼마를 투입하셨습니까? : "))
price = int(input("물건의 값은 얼마입니까? : "))
change = moneyin - price

change500 = change // 500
print("500원 동전의 개수 : ", change500)
change = change % 500
change100 = change // 100
print("100원 동전의 개수 : ", change100)
change = change % 100
change50 = change // 50
print("50원 동전의 개수 : ", change50)
change = change % 50
change10 = change // 10
print("10원 동전의 개수 : ", change10)

change = moneyin - price
change500 = change // 500
print("500원 동전의 개수 : ", change500)
change100 = (change - change%500*500) // 100
print("100원 동전의 개수 : ", change100)
change50 = (change - change%500*500 - change100*100) // 50
print("50원 동전의 개수 : ", change50)
change10 = (change - change%500*500 - change100*100) - change50*50 // 10
print("10원 동전의 개수 : ", change10)

input()
