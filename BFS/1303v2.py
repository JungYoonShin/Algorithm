import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
battleground = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, color):
  sum = 0
  queue = deque([(x, y)])
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    sum += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
        if battleground[nx][ny] == color:
          queue.append((nx, ny))
          visited[nx][ny] = True
  return sum


sum_w, sum_b = 0, 0
for i in range(m):
  for j in range(n):
    if battleground[i][j] == 'W' and not visited[i][j]:
      sum_w += bfs(i, j, 'W')**2
    elif battleground[i][j] == 'B' and not visited[i][j]:
      sum_b += bfs(i, j, 'B')**2
print(sum_w, sum_b)
