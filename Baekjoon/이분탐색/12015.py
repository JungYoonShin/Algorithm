import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def binary_search(target):
    start, end = 0, len(lis)

    while start <= end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid

        elif lis[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start



lis = [nums[0]]
for i in range(1, n):
    target = nums[i]

    if lis[-1] < target:
        lis.append(target)
    elif lis[-1] > target:
        idx = binary_search(target)
        lis[idx] = target

print(len(lis))
