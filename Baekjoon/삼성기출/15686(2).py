import sys
from itertools import combinations


input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken.append((i, j))
        elif maps[i][j] == 1:
            home.append((i, j))

visited = [False] * len(chicken)

root = []
result = 1e9
def back_tracking(start, cnt):
    global root, result
    if cnt == m:
        sum = 0
        for home_x, home_y in home:
            minn = 1e9
            for chicken_x, chicken_y in root:
                minn = min(minn, abs(chicken_x-home_x) + abs(chicken_y-home_y))
            sum += minn

        result = min(sum, result)


    for i in range(start, len(chicken)):
        if chicken[i] not in root:
            root.append(chicken[i])
            back_tracking(i+1, cnt+1)
            root.pop()

back_tracking(0, 0)
print(result)
