import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline


dx = [0, 0 , 1, -1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def dfs(x, y):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<h and 0<=ny<w:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    visited = [[False for _ in range(w)] for _ in range(h)]
    result = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                result += 1
    print(result)


