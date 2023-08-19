import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
reversed_nums = nums[::-1]
up = [1] * n
down = [0] * n

for i in range(1, n):
  for j in range(i):
    if nums[j] < nums[i]:
      up[i] = max(up[i], up[j] + 1)
    if reversed_nums[j] < reversed_nums[i]:
      down[i] = max(down[i], down[j] + 1)

down = down[::-1]
sum = 0
for i in range(n):
  sum = max(sum, down[i] + up[i])
print(sum)

##어렵다....참고 레퍼런스: https://coooco.tistory.com/104