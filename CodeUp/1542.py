# 함수로 prime 또는 composite 출력하기
def f(key):
    if key%2!=0:
        for i in range(2, key):
            if key%i==0:
                print("composite")
                exit()
        print("prime")
    elif key == 2:
        print("prime")
    else:
        print("composite")

f(int(input()))