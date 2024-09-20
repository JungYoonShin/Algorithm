import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
battleground = []

for _ in range(m):
  battleground.append(list(input().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * n for _ in range(m)]


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
    if not visited[i][j]:
      sum = bfs(i, j, battleground[i][j])
      if battleground[i][j] == 'W':
        sum_w += sum * sum
      else:
        sum_b += sum * sum
print(sum_w, sum_b)
