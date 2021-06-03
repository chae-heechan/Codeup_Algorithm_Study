# 이상한 출석 번호 부르기1
checkCount = int(input())
numbers = map(int, input().split())
attendance = [0]*23
for count in numbers:
    attendance[count-1] += 1
for count in range(23):
    print(attendance[count], end=" ")