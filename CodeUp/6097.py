# 설탕과자 뽑기
h, w = map(int, input().split())
times = int(input())

checkerboard = [[0 for i in range(w)] for j in range(h)]

for count in range(times):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            checkerboard[x-1][y+i-1] = 1
    elif d == 1:
        for j in range(l):
            checkerboard[x+j-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(checkerboard[i][j], end=" ")
    print()