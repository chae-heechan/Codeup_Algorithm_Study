# 함수로 plus/minus/0 판별하기
def f(key):
    if key>0:
        print("plus")
    elif key==0:
        print("zero")
    else:
        print("minus")

f(int(input()))