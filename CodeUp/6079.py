# 언제까지 더해야 할까?
a = int(input())
sum = 0
count = 0
while sum < a:
    count += 1
    sum += count
print(count)