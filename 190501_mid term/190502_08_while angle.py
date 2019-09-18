import turtle

# n을 입력받아서 n각형을 그리자
t = turtle.Turtle()

n = int(input("몇각형을 그리시겠어요? : "))
k = 1

print(n,"각형을 그리겠습니다.")

while k<=n:
    t.fd(10)
    t.rt(360/n)
    k += 1 # 이걸 안하면 무한 루프
