import sys

input = sys.stdin.readline

# 문자열의 뒤에 A를 추가한다.
# 문자열을 뒤집고 뒤에 B를 추가한다.
#
# B -> ABBA

S = input().rstrip()
T = input().rstrip()

while True:
    if len(T) == len(S):
        print(0)
        break

    if T[-1] == "A":
        T = T[:-1]

    else:
        T = T[:-1]
        T = T[::-1]

    if T == S:
        print(1)
        break
