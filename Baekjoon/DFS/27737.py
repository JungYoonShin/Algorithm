import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                dfs(nx, ny)


need = 0
use_seed = False
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 0:
            cnt = 0
            dfs(i,j)
            need += math.ceil(cnt / k)
            use_seed = True
if not use_seed:
    print('IMPOSSIBLE')
elif need > m:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(m-need)

