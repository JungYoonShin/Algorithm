import sys
from collections import deque

input = sys.stdin.readline

n =  int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1
b -= 1

visited = [False] * n

def bfs():
    q = deque([[a, 0]])
    visited[a] = True

    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt

        #오른쪽으로 이동
        for i in range(now, n, bridge[now]):
            if not visited[i]:
                visited[i] = True
                q.append([i, cnt+1])

        #왼쪽으로 이동
        for i in range(now-bridge[now], -1, -bridge[now]):
            if not visited[i]:
                visited[i] = True
                q.append([i, cnt + 1])

result = bfs()
if result == None:
    print(-1)
else:
    print(result)
