# 성실한 개미
checkerboard = [[0 for j in range(10)] for i in range (10)]
count = 0
for i in range(10):
    row = map(int, input().split())
    for point in row:
        checkerboard[i][count] = point
        count += 1
    count = 0

print(checkerboard)