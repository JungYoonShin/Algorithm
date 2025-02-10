import sys

input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

left, right = 0, max(times) * m

times.sort()

while left <= right:
    mid = (left + right) // 2

    people = 0
    for time in times:
        people += mid // time

    if people >= m:
        result = mid
        right = mid - 1
    else:
        left = mid + 1
print(result)
