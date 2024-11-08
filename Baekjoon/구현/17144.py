import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = []
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(r):
    graph.append(list(map(int, input().split())))

cleaner = []
dust = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            cleaner.append((i, j))
        elif graph[i][j] > 0:
            dust.append((i, j, graph[i][j]))

#미세먼지 확산  
def diffusion():
    while dust:
        cnt = 0
        x, y, value = dust.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (nx, ny) not in cleaner:
                    graph[nx][ny] += (value // 5)
                    cnt += 1
        graph[x][y] -= (value // 5) * cnt

def clean(a, b):
    #위쪽 청소(반시계 방향: 우 -> 상 -> 좌 -> 하)
    direction = 0
    x, y = a, 1
    before = 0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == a and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

    #아래쪽 청소(반시계 방향: 우 -> 하 -> 왼 -> 상)
    direction = 0
    x, y = b, 1
    before = 0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == b and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction -= 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

a = cleaner[0][0]
b = cleaner[1][0]

for _ in range(t):
    diffusion()
    clean(a, b)
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                dust.append((i, j, graph[i][j]))
sum = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            sum += graph[i][j]
print(sum)
