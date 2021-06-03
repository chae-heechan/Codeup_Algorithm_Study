# 이상한 출석 번호 부르기2
checkCount = int(input())
numbers = map(int, input().split())
l = []*checkCount
for number in numbers:
    l.append(number)
for number in reversed(l):
    print(number, end=" ")