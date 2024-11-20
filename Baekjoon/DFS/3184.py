import sys

sys.setrecursionlimit(10**6) #런타임 에러때문에 추가

input = sys.stdin.readline


r, c = map(int, input().split())
madang = []
visited = [[False for _ in range(c)] for _ in range(r)]

for _ in range(r):
    madang.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

o, v  = 0, 0
def dfs(x, y):
    global o, v
    visited[x][y] = True

    if madang[x][y] == "o":
        o += 1
    elif madang[x][y] == "v":
        v += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:

            if madang[x][y] == "#":
                continue
            dfs(nx, ny)


sum_o, sum_v = 0, 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and madang[i][j] != "#":
            o, v = 0, 0
            dfs(i, j)
            if o > v:
                sum_o += o
            else:
                sum_v += v
print(sum_o, sum_v)
