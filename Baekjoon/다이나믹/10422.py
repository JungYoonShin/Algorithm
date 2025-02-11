import sys

input = sys.stdin.readline


t = int(input())
dp = [0] * 5001
dp[0] = 1

for n in range(2, 5001, 2):
    for j in range(2, n+1, 2):
        dp[n] += dp[j-2] * dp[n-j]
    dp[n] %= 1000000007

for _ in range(t):
    l= int(input())
    print(dp[l])
