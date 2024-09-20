import sys 
input = sys.stdin.readline

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  #빨간집
  home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0]
  #초록집
  home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1]
  #파란집
  home[i][2] = min(home[i-1][0], home[i-1][1]) + home[i][2]

print(min(home[n-1]))