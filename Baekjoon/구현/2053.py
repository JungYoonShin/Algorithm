import sys

input = sys.stdin.readline

n = int(input())

nums = []
for i in range(1, 10):
    for j in range(1, 10):
        for z in range(1, 10):
            if i != j and j != z and i != z:
                nums.append(str(i) + str(j) + str(z))

for _ in range(n):
    n, s, b = map(int, input().split())
    n = str(n)
    new_nums = []

    for num in nums:
        strike, ball = 0, 0
        for i in range(3):
            if num[i] == n[i]:
                strike += 1
            elif n[i] in num:
                ball += 1
        if strike == s and ball == b:
            new_nums.append(num)
    nums = new_nums

print(len(nums))
