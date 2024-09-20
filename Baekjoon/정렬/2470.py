import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

left_pointer = 0
right_pointer = n - 1

result = [0, 0]
before_sum = 100000000000
while left_pointer < right_pointer:
  sum = liquid[left_pointer] + liquid[right_pointer]
  if abs(sum) < before_sum:
    result[0] = liquid[left_pointer]
    result[1] = liquid[right_pointer]
    before_sum = abs(sum)
  if sum > 0:
    right_pointer -= 1
  if sum < 0:
    left_pointer += 1
  if sum == 0:
    break
print(result[0], result[1])

###역시 골드는 어렵구나.. 접근 자체가 어렵고, 투포인터는 처음듣는 듯..?
