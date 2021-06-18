# 함수로 원하는 값의 위치 리턴하기 1
count = int(input())
numbers = [0] * count
number = map(int, input().split())

times = 0
for element in number:
    numbers[times] = element
    times += 1

find_number = int(input())
find_index = -1
times = 0

for find in numbers:
    if find_number == find:
        find_index = times+1
        break
    times += 1

print(find_index) 
