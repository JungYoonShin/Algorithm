import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        result[i][j] = max(result[i - 1][j], result[i][j - 1]) + graph[i-1][j-1]

print(result[n][m])
