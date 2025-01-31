import sys

w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
my_dir, my_loc = map(int, sys.stdin.readline().split())


def calc_abs_dist(direction, location):
    if direction == 1:  # 북쪽
        return location
    elif direction == 2:  # 남쪽
        return w + h + w - location
    elif direction == 3:  # 서쪽
        return w + h + w + h - location
    elif direction == 4:  # 동쪽
        return w + location

def calc_min_dist(direction, location):
    abs_dist = abs(calc_abs_dist(direction, location) - my_abs_dist)
    opposite_dist = 2 * (w + h) - abs_dist
    return min(abs_dist, opposite_dist)

ans = 0
my_abs_dist = calc_abs_dist(my_dir, my_loc)
for i in arr:
    ans += calc_min_dist(i[0], i[1])
print(ans)
