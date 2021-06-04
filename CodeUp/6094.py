# 이상한 출석 번호 부르기3
checkCount = int(input())
numbers = map(int, input().split())
attendance = []*(checkCount+1)

for num in numbers:
    attendance.append(num)
minNumber = attendance[0]
for count in range(checkCount):
    if minNumber > attendance[count]:
        minNumber = attendance[count]
print(minNumber)