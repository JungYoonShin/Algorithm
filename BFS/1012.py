import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
  queue = deque([(x, y)])
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = 0
        
        
T = int(input())
for _ in range(T):
  m, n, k = list(map(int, input().split()))
  graph = [[0] * m for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1

  cnt = 0
  for a in range(n):
    for b in range(m):
      if graph[a][b] == 1:
        bfs(graph, a, b)
        cnt += 1
  print(cnt)
    