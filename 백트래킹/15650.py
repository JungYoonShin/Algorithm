import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [0] * (n+1)
result = [0]

def backtracking(count):
  global result
  if count == m:
    print(*result[1:])
    return
  for i in range(1, n+1):
    if map[i] == 0 and i > result[-1]:
      map[i] = 1
      result.append(i)
      backtracking(count+1)
      map[i] = 0
      result.pop()
backtracking(0)