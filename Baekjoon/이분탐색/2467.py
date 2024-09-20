import sys

input = sys.stdin.readline
n = int(input())
fluid = list(map(int, input().split()))

left_pointer = 0
right_pointer = n - 1
min_sum = 999999999999
result = []
while left_pointer < right_pointer:
  sum = fluid[left_pointer] + fluid[right_pointer]
  if abs(sum) <= min_sum:
    min_sum = abs(sum)
    result = []
    result.append((fluid[left_pointer], fluid[right_pointer]))
  ##합이 양수이면(오른쪽 포인터를 왼쪽으로 한 칸 이동)
  if sum >= 0:
    right_pointer -= 1
  ##합이 음수이면(왼쪽 포인터를 오른쪽으로 한 칸 이동)
  elif sum < 0:
    left_pointer += 1

print(result[0][0], result[0][1])

##15번째 문장이 없어서 계속 틀렸었다.....ㅎㅎ