import sys 
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]

def sum(k):
  if k == 1:
    return 1
  elif k == 2:
    return 2
  elif k == 3:
    return 4
  else:
    return sum(k-1) + sum(k-2) + sum(k-3)
  
for num in nums: print(sum(num))