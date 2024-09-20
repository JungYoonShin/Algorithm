import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
  sum = 0
  queue = deque([(x, y)])
  graph[x][y] = 0
  while queue:
    x, y = queue.popleft()
    sum += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = 0
  return sum


result = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      result.append(bfs(i, j))

if len(result) == 0:
  print(len(result))
  print(0)
else:
  print(len(result))
  print(max(result)) 