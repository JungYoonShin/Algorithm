import sys
input = sys.stdin.readline

n = int(input())
graph = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n+1)

answer = []
result = []
def dfs(now, start):
    togo = graph[now]
    visited[now] = True
    if not visited[togo]:
        dfs(togo, start)
    elif visited[togo] and togo == start:
        result.append(start)

for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)
print(len(result))
print(*sorted(result), sep="\n")




