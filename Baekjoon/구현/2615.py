import sys

input = sys.stdin.readline

graph = []
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for _ in range(19):
    graph.append(list(map(int, input().split())))

for x in range(19):
    for y in range(19):
        if graph[x][y] != 0:

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while True:
                    if 0 <= nx < 19 and 0 <= ny < 19 and graph[x][y] == graph[nx][ny]:
                        cnt += 1
                        if cnt == 5:
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19:
                                if graph[x-dx[i]][y-dy[i]] == graph[x][y]:
                                    break
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19:
                                if graph[nx+dx[i]][ny+dy[i]] == graph[nx][ny]:
                                    break
                            print(graph[x][y])
                            print(x+1, y+1)
                            exit()
                        nx += dx[i]
                        ny += dy[i]
                    else:
                        break
print(0)
