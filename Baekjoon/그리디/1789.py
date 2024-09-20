import sys
input = sys.stdin.readline

s = int(input())
i = 0
sum = 0
while True:
  i+=1
  sum += i
  if sum == s:
    print(i)
    break
  elif sum > s:
    print(i-1)
    break
## 처음에 sum == s에 대한 조건문을 안써서 틀렸다,,,