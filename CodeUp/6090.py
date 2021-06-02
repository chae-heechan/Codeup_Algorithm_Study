# 수 나열하기3
a, b, c, d = map(int, input().split())
result = a
for count in range(d-1):
    result = result*b+c
print(result)