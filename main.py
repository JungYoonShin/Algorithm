import sys
sys.setrecursionlimit(10**6)  #이거 없으면 런타임에러가 난다....

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n + 1)]
result = [0] * (n + 1)

for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n + 1)
root = [0] *(n+1)

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      root[i] = v
      dfs(i)
dfs(1)
# for i in range(2, n+1):
#   value = dfs(graph, i, 0)
#   result[i] = value

print(*root[2:], sep="\n")
  
