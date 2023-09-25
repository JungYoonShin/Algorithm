import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dikstra():
  visited[0][0] = 1
  q = []
  heappush(q, (0, 0, 0))
  while q:
    cost, x, y = heappop(q)
    if x == n - 1 and y == n - 1:
      print(cost)
      return
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        #검은방일때
        if graph[nx][ny] == 0:
          heappush(q, (cost + 1, nx, ny))
        else:
          heappush(q, (cost, nx, ny))


dikstra()

##다익스트라를 사용한 문제..처음 풀어보는듯(heapq에 대해 알게됨) -> 이거는 최소힙을 사용했다.
