import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
shark_size = 2


def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    q = deque([(x, y, 0)])
    able = []
    visited[x][y] = 1

    while q:
        x, y, distance = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if graph[nx][ny] <= shark_size:
                        visited[nx][ny] = True
                        q.append((nx, ny, distance + 1))
                        if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                            able.append((nx, ny, distance + 1))

    return sorted(able, key=lambda x: (x[2], x[0], x[1]))



time = 0
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j

while True:
    s = bfs(shark_x, shark_y)
    if len(s) == 0:
        break

    x, y, t = s[0]

    time += t
    graph[x][y], graph[shark_x][shark_y] = 0, 0
    cnt += 1
    shark_x, shark_y = x, y
    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(time)
