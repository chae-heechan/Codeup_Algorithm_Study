# 참/거짓이 서로 다를 때에만 참 출력하기
a, b = map(bool, map(int, input().split()))
print((a and not b) or (not a and b))