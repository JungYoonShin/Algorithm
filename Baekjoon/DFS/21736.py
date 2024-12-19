import sys
sys.setrecursionlimit(10**6) # 재귀 제한 늘이기
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
campus = []
for _ in range(n):
    campus.append(list(input().rstrip()))

visited = [[False] * m for _ in range(n)]

cnt = 0
def dfs(x, y):
    global cnt
    visited[x][y] = True
    if campus[x][y] == 'P':
        cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and campus[nx][ny] != "X":
                dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            dfs(i, j)
if cnt == 0:
    print("TT")
else:
    print(cnt)
