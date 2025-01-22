import sys

input = sys.stdin.readline

result = 0
a, k = map(int, input().split())
while True:
    if k == a:
        print(result)
        break

    if k % 2 == 0 and k // 2 >= a:
        result += 1
        k //= 2
    else:
        result += 1
        k = k - 1
