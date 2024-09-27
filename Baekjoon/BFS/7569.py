import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

tomato = []
for _ in range(h):
    graph = [list(map(int, input().split())) for _ in range(n)]
    tomato.append(graph)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()
def bfs():

    while queue:
        x, y, z = queue.popleft()
        visited[x][y][z] = True

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if not visited[nx][ny][nz] and tomato[nx][ny][nz] == 0:
                    queue.append((nx, ny, nz))
                    tomato[nx][ny][nz] = tomato[x][y][z]+1
                    visited[nx][ny][nz] = True


answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))

bfs()

for floor in tomato:
    for a in floor:
        for b in a:
            if b == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(a))

print(answer-1)
