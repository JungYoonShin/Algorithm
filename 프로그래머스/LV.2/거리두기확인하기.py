from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, place):
    visited = [[False]*5 for _ in range(5)]
    q = deque([(x, y, 0)])
    visited[x][y] = True
    
    while q:
        x, y, depth = q.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if place[nx][ny] == 'O':
                    visited[nx][ny] = True
                    q.append((nx, ny, depth + 1))
                        
                if depth <= 1 and place[nx][ny] == 'P':
                    return True  # 거리두기 위반
                    
    return False  # 거리두기 위반 없음

def solution(places):
    answer = []
    
    for place in places:
        violated = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(i, j, place):
                        answer.append(0)
                        violated = True
                        break
            if violated:
                break
        if not violated:
            answer.append(1)
    
    return answer
