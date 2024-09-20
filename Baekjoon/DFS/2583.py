import sys
from collections import deque

input = sys.stdin.readline
m, n, k = list(map(int, input().split()))

graph = [[0] * n for _ in range(m)]
for _ in range(k):
  lx, ly, rx, ry = map(int, input().split())
  for j in range(ly, ry):
    for p in range(lx, rx):
      graph[j][p] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
  queue = deque([(x, y)])
  graph[x][y] = 1
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<= nx < n and 0<= ny < m and graph[ny][nx] == 0:
        graph[ny][nx] = 1
        cnt += 1
        queue.append((ny, nx))
  return cnt

area = []
for i in range(m):
  for j in range(n):
    if graph[i][j] == 0:
      area.append(bfs(i, j, 1))
area.sort()
print(len(area))
print(*area)


