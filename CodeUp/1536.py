# 함수로 가장 작은 값 리턴하기
count = int(input())
lst = [0]*count
elements = map(int, input().split())
times = 0

for i in elements:
    lst[times] = i
    times += 1

def f():
    min_num = lst[0]
    for i in range(count):
        if min_num < lst[i]:
            max_num = lst[i]
    print(min_num)

f()