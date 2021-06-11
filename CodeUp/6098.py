# 성실한 개미
checkerboard = [[0 for j in range(10)] for i in range (10)]
count = 0
for i in range(10):
    row = map(int, input().split())
    for point in row:
        checkerboard[i][count] = point
        count += 1
    count = 0

x, y = 1, 1
while(True):
    if checkerboard[x][y]==2:       # 현 위치가 2일 경우
        checkerboard[x][y] = 9
        break
    else:                           # 현 위치가 2가 아닐 경우
        checkerboard[x][y] = 9
        if checkerboard[x][y+1] == 1:       # 오른쪽이 1일 경우
            if checkerboard[x+1][y] == 1:   # 아래쪽이 1일 경우
                break
            else:                   # 아래쪽이 0이나 2일 경우
                x += 1
        else:                       # 오른족이 0이나 2일 경우
            y += 1

for i in range(10):     # 10번 반복
    for j in range(10):
        print(checkerboard[i][j], end=" ")
    print()