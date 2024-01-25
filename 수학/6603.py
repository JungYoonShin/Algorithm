import sys
from collections import deque

input = sys.stdin.readline


def dfs(depth, index):
  if depth == 6:
    print(*lotto)
    return

  for i in range(index, k):
    lotto.append(s[i])
    dfs(depth + 1, i + 1)
    lotto.pop()


visited = [0] * 20
while True:
  num = list(map(int, input().split()))
  lotto = deque()
  k = num[0]
  s = num[1:]
  if k == 0:
    break
  dfs(0, 0)
  print()
