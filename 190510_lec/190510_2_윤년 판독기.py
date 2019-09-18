# 스크립트 모드입니다
# 윤년인지 아닌지를 판단하는 프로그램을 만듭시다

year = int(input("연도를 입력하시오: "))
 
if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    print("%s 년은 윤년입니다." %year)
else :
    print(year,"년은 윤년이 아닙니다.") 
