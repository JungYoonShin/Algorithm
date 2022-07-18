k = int(input())
#한 줄씩 입력받기
#p = list(map(int, stdin.read().split()))
nums = []
for _ in range(k):
  nums.append(int(input()))

result = 0
new_list = []
for i in nums:
  if i != 0:
    new_list.append(i)
  elif i == 0:
    new_list.pop()

  
print(sum(new_list))