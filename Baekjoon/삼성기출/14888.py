import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())

max_result = -10**9
min_result = 10**9

def dfs(i, result):
    global add, minus, mul, div, max_result, min_result

    if i == n:
        max_result = max(result, max_result)
        min_result = min(result, min_result)

    if add > 0:
        add -= 1
        dfs(i+1, result + nums[i])
        add += 1
    if minus > 0:
        minus -= 1
        dfs(i+1, result - nums[i])
        minus += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, result * nums[i])
        mul += 1
    if div > 0:
        div -= 1
        if result < 0:
            dfs(i+1, -(abs(result) // nums[i]))
        else:
            dfs(i+1, result // nums[i])
        div += 1

dfs(1, nums[0])
print(max_result)
print(min_result)
