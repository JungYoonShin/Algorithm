import sys

input = sys.stdin.readline
t = int(input())
num = [0, 1, 1, 1, 2, 2] + [0 for _ in range(97)]


def pado(x):
    if num[x]:
        return num[x]

    else:
        num[x] = pado(x-1) + pado(x-5)
        return num[x]
for _ in range(t):
    n = int(input())
    print(pado(n))

