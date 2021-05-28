# 점수 입력받아 평가 출력하기
a = int(input())
if a >= 90:
    print("A")
elif 90 > a >= 70:
    print("B")
elif 70 > a >= 40:
    print("C")
else:
    print("D")