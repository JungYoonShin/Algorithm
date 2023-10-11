#14502_연구소_bfs_gold5

from collections import deque
import copy
import sys
input = sys.stdin.readline

d = [[-1,0],[1,0],[0,-1],[0,1]]

result = 0
def bfs():
  queue = deque()
  new_map = copy.deepcopy(map)
  #바이러스가 퍼져있는 곳 위치 저장 
  for i in range(n):
    for j in range(m):
      if new_map[i][j] == 2:
        queue.append((i, j))
        
  #바이러스 퍼트리기
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]
      if 0<=dx<n and 0<=dy<m and new_map[dx][dy] == 0:
        new_map[dx][dy] = 2
        queue.append((dx, dy))
        
  #바이러스 안 퍼진곳 세기
  global result 
  cnt = 0
  for i in range(n):
    for j in range(m):
      if new_map[i][j] == 0:
        cnt += 1
  result = max(cnt, result)

def make_wall(count):
  if count == 3:
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if map[i][j] == 0:
        map[i][j] = 1
        make_wall(count+1)
        #백트래킹(벽을 허문다)
        map[i][j] = 0            

n, m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)
print(result)

###꼭 다시풀어보기, 특히 백트래킹 공부하자!!
## python3으로 돌리면 시간초과남 