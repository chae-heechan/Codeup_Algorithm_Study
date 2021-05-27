# 정수 3개 입력받아 짝/홀 출력하기
a = []
a.extend(map(int, input().split()))
for count in a:
    if count%2==0:
        print("even")
    else:
        print("odd")
