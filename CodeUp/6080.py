# 주사위 2개 던지기
a, b = map(int, input().split())
for aloop in range(1, a+1):
    for bloop in range(1, b+1):
        print(aloop, bloop)