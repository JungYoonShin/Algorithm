import sys
from copy import deepcopy

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

maps = []
fish = [[] for _ in range(16)]
for i in range(4):
    m = list(map(int, input().split()))
    temp = []
    for j in range(0, 7, 2):
        temp.append([m[j]-1, m[j+1]-1])
        fish[m[j]-1] = [i, j // 2]
    maps.append(temp)

result = 0
def dfs(x, y, d, sum):
    global result, maps, fish
    #물고기 움직임
    fish_move(x, y)
    while True:
        shark_x, shark_y = x + dx[d], y + dy[d]
        if not 0<= shark_x < 4 or not 0<= shark_y < 4: #상어가 더이상 이동할 곳 없음
            result = max(result, sum)
            return
        if not maps[shark_x][shark_y]: #물고기 없음
            x, y = shark_x, shark_y
            continue

        temp_maps, temp_fish = deepcopy(maps), deepcopy(fish)
        location, n = fish[maps[shark_x][shark_y][0]], maps[shark_x][shark_y]
        fish[maps[shark_x][shark_y][0]], maps[shark_x][shark_y] = [], [] #물고기 먹음
        dfs(shark_x, shark_y, n[1], sum + n[0] + 1)
        #되돌리기
        maps, fish = temp_maps, temp_fish
        fish[maps[shark_x][shark_y][0]], maps[shark_x][shark_y] = location, n
        x, y = shark_x, shark_y


def fish_move(shark_x, shark_y):
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1] #물고기 위치
            for _ in range(9):
                d = maps[x][y][1]
                nx, ny = x + dx[d], y + dy[d]
                if not 0<= nx < 4 or not 0<= ny < 4 or (nx == shark_x and ny == shark_y):
                    maps[x][y][1] = (maps[x][y][1] + 1) % 8
                    continue
                if maps[nx][ny]:
                    fish[maps[nx][ny][0]] = [x, y]
                maps[x][y], maps[nx][ny] = maps[nx][ny], maps[x][y]
                fish[i] = [nx, ny]
                break

d, num = maps[0][0][1], maps[0][0][0]
fish[maps[0][0][0]], maps[0][0] = [], []
dfs(0, 0, d, num + 1)
print(result)

#https://yeon-code.tistory.com/79
