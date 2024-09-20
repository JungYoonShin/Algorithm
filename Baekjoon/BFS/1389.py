import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(start, visited):
  queue = deque([start])
  result = [0] * (n+1) 
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        result[i] = result[v] + 1
        queue.append(i)
        visited[i] = True
  return result



for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

min = 10000
for i in range(1, n+1):
  visited = [False] * (n+1)
  result = bfs(i, visited)
  if sum(result) < min:
    min = sum(result)
    kevin = i
print(kevin)
  