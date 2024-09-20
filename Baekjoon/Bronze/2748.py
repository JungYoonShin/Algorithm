import sys

input = sys.stdin.readline
n = int(input())
F = [0] * (n+2)
F[0], F[1] = 0, 1

for i in range(2, n+1):
  F[i] = F[i-1] + F[i-2]

print(F[n])