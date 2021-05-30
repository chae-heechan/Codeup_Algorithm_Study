# 짝수 합 구하기
sum = 0
number = int(input())
for count in range(number+1):
    if count%2==0:
        sum +=count
print(sum)