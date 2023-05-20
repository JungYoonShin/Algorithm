import sys

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
def dfs(x, y):
  global count
  if x <0 or x >= n or y < 0 or y >= n:
    return
  if graph[x][y] == 1:
    count += 1
    graph[x][y] = 0
    for i in range(4):
      dfs(x + dx[i], y + dy[i])

houses = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      dfs(i, j)
      houses.append(count)
      count = 0

print(len(houses))
houses.sort()
print(*houses, sep='\n')

##처음에 정렬안해서 틀림
## 항상 입력 잘 받는 거에 신경쓰자..ㅎㅎ