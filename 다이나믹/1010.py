import sys

input = sys.stdin.readline
t = int(input())

#방법1(다이나믹 프로그래밍)
for _ in range(t):
  a, b = map(int, input().split())
  dp = [[0] * (b+1) for _ in range(a+1)]
  for i in range(1, a+1):
    for j in range(1, b+1):
      if i == j:
        dp[i][j] = 1
      elif i == 1:
        dp[i][j] = j
      else:
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
  print(dp[a][b])

#방법2(조합)
##mCn = m! 나누기 (m-n)!n!
