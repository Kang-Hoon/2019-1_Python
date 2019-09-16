#스크립트 모드입니다.
#화씨온도를 섭씨온도로 변환해준다.

far = int(input("Farenheit ? : "))
cel = (far-32)*5/9
print( "cel = ", cel ) #나눌 때에 5.0, 9.0으로 나누지 않아도 어차피 나누면 실수로 나타내진다.

input()

