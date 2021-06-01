# 3의 배수는 통과
number = int(input())
for count in range(1, number+1):
    if count%3!=0:
        print(count, end=" ")