# 월 입력받아 계절 출력하기
a = int(input())
if a==12 or a==1 or a==2:
    print("winter")
elif a // 3 == 1:
    print("spring")
elif a // 3 == 2:
    print("summer")
else:
    print("fall")