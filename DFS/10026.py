import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

num = int(input())
district = [list(input().rstrip()) for _ in range(num)]

visited = [[False] * num for _ in range(num)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  visited[x][y] = True
  curr_color = district[x][y]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<num and 0<=ny<num:
      if not visited[nx][ny] and district[nx][ny] == curr_color:
        dfs(nx, ny)
  
#적록색약 아닐 때
able = 0
for i in range(num):
  for j in range(num):
    if not visited[i][j]:
      dfs(i, j)
      able += 1

#적록색약일 때
for i in range(num):
  district[i] = list(map(lambda x : "G" if x == "R" else x, district[i]))
  
visited = [[False] * num for _ in range(num)]
disable = 0
for i in range(num):
  for j in range(num):
    if not visited[i][j]:
      dfs(i, j)
      disable += 1
      
print(able, disable)

##sys.setrecursionlimit(1000000) 이거 없이 처음에 했더니 런타임 에러남! 31,32 lambda 시도해봄 