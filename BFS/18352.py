from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())

graph = [[] for _ in range(n + 1)]
# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#BFS
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([x])
while q:
  out = q.popleft()
  for next in graph[out]:
    if distance[next] == -1:
      distance[next] = distance[out] + 1
      q.append(next)

flag = 0
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    flag = 1

if flag == 0:
  print(-1)
