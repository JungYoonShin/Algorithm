import sys
from collections import deque

input = sys.stdin.readline


n, m, r = map(int, input().split())
visited = [False] * (n+1)
visited[r] = True
q = deque([r])
cnt = 1
result = [0] * (n+1)
result[r] = 1

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

while q:
    v = q.popleft()
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            result[i] = cnt
            q.append(i)
print(*result[1:], sep="\n")
