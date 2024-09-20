import sys
input = sys.stdin.readline

N = int(input())
plus = []
minus = []
result = 0

for _ in range(N):
  num = int(input())
  if num <=0 :
    minus.append(num)
  elif num >= 1:
    plus.append(num)
  ##1인 경우는 무조건 더하는 게 커진다
  else:
    result += num
    
plus.sort(reverse=True)
minus.sort()
##양수
for i in range(0, len(plus), 2):
  if i+1 >= len(plus):
    result += plus[i]
  else:
    result += plus[i] * plus[i+1]
##음수
for i in range(0, len(minus), 2):
  if i+1 >= len(minus):
    result += minus[i]
  else:
    result += minus[i] * minus[i+1]

print(result)
    
###처음 골드 풀어봄,,, 경우의 수를 나눠서 푸는게 넘 어렵...그래도 늘겠지!!!