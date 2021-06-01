# 빛 섞어 색 만들기
r, g, b = map(int, input().split())
count = 0
for rcount in range(r):
    for gcount in range(g):
        for bcount in range(b):
            print(rcount, gcount, bcount)
            count += 1
print(count)