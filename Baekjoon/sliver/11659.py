import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

prefixSum = [0] * (n + 1)
prefixSum[0], prefixSum[1] = 0, num[0]
for i in range(2, n + 1):
  prefixSum[i] = prefixSum[i - 1] + num[i - 1]

for _ in range(m):
  i, j = map(int, input().split())
  print(prefixSum[j] - prefixSum[i - 1])
