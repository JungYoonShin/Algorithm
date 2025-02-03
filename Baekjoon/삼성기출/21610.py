import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]

rx = [0, -1, -1, -1, 0, 1, 1, 1]
ry = [-1, -1, 0, 1, 1, 1, 0, -1]

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for move in moves:
    d, s = move[0]-1, move[1] % n

    new_cloud = set()
    while cloud:
        x, y = cloud.pop()
        nx = (x + s*rx[d]) % n
        ny = (y + s*ry[d]) % n

        board[nx][ny] += 1
        new_cloud.add((nx, ny))

    for nc in new_cloud:
        cnt = 0
        for i in range(4):
            x, y = nc
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < n:
                if board[nx][ny] > 0:
                    cnt += 1
        board[x][y] += cnt

    for x in range(n):
        for y in range(n):
            if (x, y) not in new_cloud:
                if board[x][y] >= 2:
                    cloud.append((x, y))
                    board[x][y] -= 2
sum = 0
for x in range(n):
    for y in range(n):
        sum += board[x][y]
print(sum)
