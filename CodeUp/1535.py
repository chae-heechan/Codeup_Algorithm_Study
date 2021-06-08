# 함수로 가장 큰 값 위치 리턴하기
count = int(input())
lst = [0]*count
elements = map(int, input().split())
times = 0

for i in elements:
    lst[times] = i
    times += 1

def f():
    max_num = lst[0]
    for i in range(count):
        if max_num < lst[i]:
            max_num = lst[i]
    print(max_num)

f()