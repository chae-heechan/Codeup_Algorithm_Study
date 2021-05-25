# 둘 다 거짓일 경우만 참 출력하기
a, b = map(bool, map(int, input().split()))
print((a==False) and (b==False))