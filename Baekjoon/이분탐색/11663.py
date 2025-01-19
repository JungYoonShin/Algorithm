import sys

input = sys.stdin.readline


n, m = map(int, input().split())
spot = list(map(int, input().split()))
spot.sort()

def find_start(spot, target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if spot[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


# 끝점과 가까운 점을 찾기
def find_end(spot, target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if spot[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for _ in range(m):
    a, b = map(int, input().split())

    print(find_end(spot, b) - find_start(spot, a))
