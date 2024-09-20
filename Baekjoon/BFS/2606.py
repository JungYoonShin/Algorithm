result = 0

def dfs(i, visited):
  visited[i] = True
  for j in graph[i]:
    if not visited[j]:
      global result
      result += 1
      dfs(j, visited)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    #18번 줄 안써서 틀렸다(바이러스는 양방향으로 전파가능함으로 써줘야 함)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(1, visited)
print(result)
