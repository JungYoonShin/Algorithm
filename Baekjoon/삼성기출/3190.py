import sys
from collections import deque


input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d  = 0 # 초기 뱀 이동 방향(오른쪽)
time = 0
snakes = deque([(1, 1)])

def move():
    snake_x, snake_y = 1, 1
    global time, visited, d
    while True:
        time += 1
        nx, ny = snake_x + dx[d], snake_y + dy[d]
        #벽에 부딪히면 게임 종료
        if (0 >= nx or nx > n) or (0 >= ny or ny > n) or (nx, ny) in snakes:
            return

        #이동한 칸에 사과가 없다면, 꼬리&머리 모두 이동
        if [nx, ny] not in apple:
            a, b = snakes.popleft()
            visited[a][b] = False

        elif [nx, ny] in apple:
            apple.remove([nx, ny])

        snake_x, snake_y = nx, ny
        visited[snake_x][snake_y] = True
        snakes.append((snake_x, snake_y))

        if time in snake_move.keys():
            if snake_move[time] == 'D':
                d = (d+1)%4
            else:
                d = (d-1)%4


n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
L = int(input())
snake_move = {}
for _ in range(L):
    a, b = input().split()
    snake_move[int(a)] = b

visited = [[False for _ in range(n+1)] for  _ in range(n+1)]
move()
print(time)
