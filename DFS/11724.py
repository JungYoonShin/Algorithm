import sys

input = sys.stdin.readline

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
  
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n + 1)
dfs(graph, 1, visited)

result = 1
for i in range(1, n+1):
  if not visited[i]:
    result += 1
    dfs(graph, i, visited)
print(result)



##약간 참고해서 구현, 22~부터는 스스로 구현