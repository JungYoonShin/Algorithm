import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num = list(set(num))
num.sort()
dict = [-1]


def back():
  if len(dict) == m + 1:
    print(*dict[1:])
    return
  for n in num:
    dict.append(n)
    back()
    dict.pop()


back()