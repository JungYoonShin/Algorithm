import sys
import copy

input = sys.stdin.readline


n, m = map(int, input().split())

maps = []

mode = [
    [],
    [[0], [1], [2], [3]],  # 1번 CCTV
    [[0, 1], [2, 3]],  # 2번 CCTV
    [[0, 3], [1, 3], [1, 2], [0, 2]],  # 3번 CCTV
    [[0, 1, 3], [0, 2, 3], [1, 2, 3], [0, 1, 2]],  # 4번 CCTV
    [[0, 1, 2, 3]]  # 5번 CCTV
]
cctv = []

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


#cctv 위치 저장
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if 1 <= maps[i][j] <= 5:
            cctv.append([maps[i][j], i, j])

def move(maps, mode, x, y):
    for i in mode:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]

            if 0<= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = -1
                if maps[nx][ny] == 6:
                    break
            else:
                break

min_result = int(1e9)


def dfs(cnt, maps):
    global min_result
    if cnt == len(cctv):
        s = sum(row.count(0) for row in maps)
        min_result = min(min_result, s)
        return


    cctv_num, x, y = cctv[cnt]
    for i in mode[cctv_num]:
        copy_maps = copy.deepcopy(maps)
        move(copy_maps, i, x, y)
        dfs(cnt+1, copy_maps)

dfs(0, maps)
print(min_result)
