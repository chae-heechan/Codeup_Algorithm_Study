# 함수로 정수 올림 한 값 리턴하기
x = float(input())

def f(key):
    key = -int(-key//1)
    return key
print(f(x))