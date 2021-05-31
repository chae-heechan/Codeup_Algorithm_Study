# 3 6 9 게임의 왕이 되자
a = int(input())
for count in range(1, a+1):
    if count%10==3 or count%10==6 or count%10==9:
        print("X", end=" ")
    else:
        print(count, end=" ")