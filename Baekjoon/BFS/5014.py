import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
check = [0 for _ in range(F+1)]

def bfs(s):
    q = deque([s])
    check[s] = 1

    while q:
        now = q.popleft()
        if now == G:
            return check[now] - 1

        for x in (now + U, now - D):
            if 1<=x<=F and check[x] == 0:
                check[x] = check[now] + 1
                q.append(x)
    return "use the stairs"

print(bfs(S))
