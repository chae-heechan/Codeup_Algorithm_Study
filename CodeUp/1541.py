# 함수로 negative/zero/positive
def f(key):
    if key > 0:      # key가 양수일 경우
        print("positive")
    elif key == 0:   # key가 0일 경우
        print("zero")
    else:            # key가 음수일 경우
        print("negative")

f(int(input()))