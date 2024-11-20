import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
visited = [[False for _ in range(c)] for _ in range(r)]

madang = []
for _ in range(r):
    madang.append(list(input().rstrip()))

def bfs(x, y):
    queue = deque([(x, y)])
    o = 0
    v = 0
    visited[x][y] = True

    if madang[x][y] == "v":
        v += 1
    elif madang[x][y] == "o":
        o += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                if madang[nx][ny] == "#":
                    continue
                elif madang[nx][ny] == "v":
                    v += 1
                elif madang[nx][ny] == "o":
                    o += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return o, v


sheep, wolf = 0, 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and madang[i][j] != '#':
            s, w = bfs(i, j)
            if s > w:
                sheep += s
            else:
                wolf += w
print(sheep, wolf)


