import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  num = int(input())
  height = list(map(int, input().split()))
  height.sort()
  result = 0
  for i in range(len(height)-2):
    result = max(result, abs(height[i] - height[i+2]))
  print(result)