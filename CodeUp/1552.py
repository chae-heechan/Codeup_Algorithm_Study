# 함수로 소수 부분만 리턴하기
def f(number):
    return number - int(number)

print("%.14f"%f(float(input())))