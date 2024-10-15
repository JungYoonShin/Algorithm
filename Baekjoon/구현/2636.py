import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
cheese_map = [list(map(int, input().split())) for _ in range(a)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(_x, _y):
    queue = deque([(_x, _y)])
    visited[_x][_y] = True
    to_be_melted = deque()
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:

                visited[nx][ny] = True
                if cheese_map[nx][ny] == 0:
                    queue.append((nx, ny))

                elif cheese_map[nx][ny] == 1:
                    to_be_melted.append((nx, ny))

    for x, y in to_be_melted:
        cheese_map[x][y] = 0
    return len(to_be_melted)

result = []
sum = 0
while True:
    visited = [[False] * b for _ in range(a)]
    t = bfs(0, 0)
    if t == 0:
        break
    result.append(t)
    sum += 1
print(sum, result[-1], sep="\n")
