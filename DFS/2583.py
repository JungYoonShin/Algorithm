import sys

sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0] * n for i in range(m)]
for i in range(k):
  lx, ly, rx, ry = map(int, input().split())
  for j in range(ly, ry):
    for p in range(lx, rx):
      graph[j][p] = 1

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, area):
  graph[x][y] = 1
  global cnt
  cnt += 1
  for i in range(4):
    ax, ay = dx[i] + x, dy[i] + y
    if (0 <= ay < n) and (0 <= ax < m) and graph[ax][ay] == 0:
      dfs(ax, ay, cnt)
  return cnt


result = 0
area = []
for i in range(m):
  for j in range(n):
    if graph[i][j] == 0:
      answer = dfs(i, j, 0)
      area.append(answer)
      result += 1
      cnt = 0

print(result)
print(*sorted(area))
