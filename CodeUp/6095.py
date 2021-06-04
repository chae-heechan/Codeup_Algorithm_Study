# 바둑판에 흰 돌 놓기
checkerboard = [[0 for j in range(20)] for i in range(20)]

times = int(input())
for count in range(times):
    x, y = map(int, input().split())
    checkerboard[x][y] = 1

print()

for i in range(1, 20):
    for j in range(1, 20):
        print(checkerboard[i][j], end =" ")
    print()