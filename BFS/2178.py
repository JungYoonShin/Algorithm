import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
def bfs(x, y):
  queue = deque([(x, y)])
  while queue:
    print(queue)
    x, y = queue.popleft()
    for i in range(4):
      move_x = x + dx[i]
      move_y = y + dy[i]
      if 0<= move_x < n and 0<= move_y < m and graph[move_x][move_y] ==1:
        queue.append((move_x, move_y))
        graph[move_x][move_y] = graph[x][y] + 1
  return graph[n-1][m-1]
print(bfs(0, 0))

## 처음에 deque([x, y])로 함.. 