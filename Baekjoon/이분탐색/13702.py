import sys

input = sys.stdin.readline

n, k = map(int, input().split())

drinks = [int(input()) for _ in range(n)]

min = 1
max = max(drinks)

while min <= max:
    mid = (min+max) // 2

    sum = 0
    for drink in drinks:
        sum += (drink // mid)

    if sum >= k:
        result = mid
        min = mid + 1
    else:
        max = mid - 1

print(result)
