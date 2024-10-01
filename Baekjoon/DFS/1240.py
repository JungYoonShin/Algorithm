import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
sum = 0

def dfs(i, j, distance):
    global sum
    visited[i] = True
    for node in graph[i]:
        if not visited[node[0]]:
            if node[0] == j:
                sum = distance + node[1]
                return
            else:
                dfs(node[0], j, distance + node[1])

for _ in range(n-1):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))

for _ in range(m):
    i, j = map(int, input().split())
    visited = [False] * (n + 1)
    sum = 0
    dfs(i, j, 0)
    print(sum)
