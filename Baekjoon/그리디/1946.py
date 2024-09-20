import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
  N = int(input())
  scores = [list(map(int, input().split())) for _ in range(N)]
  scores.sort()

  top = 0
  result = 1

  for i in range(1, len(scores)):
    if(scores[top][1] > scores[i][1]):
      top = i
      result += 1
  print(result)

