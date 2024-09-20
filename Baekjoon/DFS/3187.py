import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * c for _ in range(r)]


def dfs(x, y):
  global sheep, wolf
  visited[x][y] = True
  if graph[x][y] == 'v':
    wolf += 1
  if graph[x][y] == 'k':
    sheep += 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and not visited[nx][
        ny] and graph[nx][ny] != '#':
      dfs(nx, ny)


wolfTotal = 0
sheepTotal = 0
for i in range(r):
  for j in range(c):
    if not visited[i][j] and graph[i][j] != '#':
      wolf, sheep = 0, 0
      dfs(i, j)
      if sheep > wolf:
        sheepTotal += sheep
      else:
        wolfTotal += wolf

print(sheepTotal, wolfTotal)
