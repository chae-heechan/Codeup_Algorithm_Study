# 문자 1개 입력받아 알파벳 출력하기
alphabet = input()
for count in range(ord("a"), ord(alphabet)+1):
    print(chr(count), end=" ")