import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

result = 0
def dfs(a, cnt):
  global result 
  cnt += 1
  if a == b:
    result = cnt
  visited[a] = True
  for i in graph[a]:
    if not visited[i]:
      dfs(i, cnt)
      
    

graph = [[] for _ in range(n + 1)]

visited = [0] * (n+1)
for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

dfs(a, 0)
if result == 0: print(-1)
else: print(result-1)
# 12
# 7 6
# 11
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
# 8 10
# 10 11
# 11 12
# 12 4
## 처음에 이 답이 7이여야하는데, 10이 나옴,, 