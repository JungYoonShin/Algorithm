import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]
visited = []

def dfs(graph, x, y, w, h):
  graph[x][y] = 0
  for i in range(8):
    move_x = x + dx[i]
    move_y = y + dy[i]
    if 0<=move_x<h and 0<=move_y<w and graph[move_x][move_y] == 1:
      dfs(graph, move_x, move_y, w, h)
    


while(True):
  graph = []
  w, h = map(int, input().split())
  if w==0 and h==0: 
    break
  result = 0
  for i in range(h):
    maps = list(map(int, input().split()))
    graph.append(maps)
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        dfs(graph, i, j, w, h)
        result += 1
  print(result)
        
      
  