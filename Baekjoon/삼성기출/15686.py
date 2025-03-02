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

#치킨 집 선택 조합 구하기
chicken_list = list(combinations(chicken, m))


def find_min(chicken_location):
    result = 0
    for home_x, home_y in home:
        minn = 1e9
        for chicken_x, chicken_y in chicken_location:
            temp = abs(chicken_x - home_x) + abs(chicken_y - home_y)
            minn = min(minn, temp)
        result += minn
    return result

sum = 1e9
for i in chicken_list:
    temp = find_min(i)
    sum = min(temp, sum)

print(sum)
