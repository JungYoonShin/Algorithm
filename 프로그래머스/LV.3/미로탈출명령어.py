import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
s = ['d', 'l', 'r', 'u']
answer = "z"
def dfs(n, m, x, y, r, c, k, cnt, ss):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):
        return
    
    if cnt == k:
        if x == r and y == c:
            answer = ss
            return
        
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 1 <= nx <= n and 1 <= ny <= m and ss < answer:
            dfs(n, m, nx, ny, r, c, k, cnt+1, ss+s[i])
    

def solution(n, m, x, y, r, c, k):
    maps = [[0 for _ in range(m)] for _ in range(n)]
    
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    
    dfs(n, m, x, y, r, c, k, 0, "")
    
    return answer
