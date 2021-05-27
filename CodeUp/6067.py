# 정수 1개 입력받아 분류하기
a = int(input())

if a<0:     # 음수면
    if a%2==0:  # 짝수면
        print("A")
    else:       # 홀수면
        print("B")
else:       # 양수면
    if a%2==0:  # 짝수면
        print("C")
    else:       # 홀수면
        print("D")
