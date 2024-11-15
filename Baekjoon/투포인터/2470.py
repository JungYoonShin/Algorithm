import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = n-1
sum = 0
min = 100000000000000000
result = []

while start < end:
    sum = liquid[start] + liquid[end]

    if abs(sum) < min:
        min = abs(sum)
        result = [liquid[start], liquid[end]]

    if sum > 0:
        end -= 1

    else:
        start += 1

print(*result)


