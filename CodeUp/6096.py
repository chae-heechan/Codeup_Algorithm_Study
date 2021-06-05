# 바둑알 십자 뒤집기
checkerboard = [[0 for j in range(19)] for i in range(19)]
count = 0
for i in range(19):
    row = map(int, input().split())
    for value in row:
        checkerboard[i][count] = value
        count += 1
    count = 0

times = int(input())
for count in range(times):
    x, y = map(int, input().split())
    for i in range(19):
        if checkerboard[x-1][i] == 0:
            checkerboard[x-1][i] = 1
        else:
            checkerboard[x-1][i] = 0
    for j in range(19):
        if checkerboard[j][y-1] == 0:
            checkerboard[j][y-1] = 1
        else:
            checkerboard[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(checkerboard[i][j], end=" ")
    print()