import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [0] * (n+1)
result = []
def backtracking(count):
  if count == m:
    print(*result)
    return
  for i in range(1, n+1):
    if map[i] == 0:
      result.append(i)
      backtracking(count+1)
      result.pop()
backtracking(0)
##다른 방법도 참고해서 올릴예정!!(10.13.2022)
      