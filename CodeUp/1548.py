# 함수로 학점 리턴하기
def f(key):
    if 100>=key>=90:
        print("A")
    elif 90>key>=80:
        print("B")
    elif 80>key>=70:
        print("C")
    elif 70>key>=60:
        print("D")
    elif 60>key:
        print("F")

f(int(input()))