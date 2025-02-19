import sys
import bisect

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

lis = [nums[0]]

for i in range(n):
    target = nums[i]
    if lis[-1] < target:
        lis.append(target)
    else:
        idx = bisect.bisect_left(lis, target)
        lis[idx] = target

print(len(lis))
