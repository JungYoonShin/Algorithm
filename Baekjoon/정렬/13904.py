import sys
input = sys.stdin.readline

homeworks = []
n = int(input())
for _ in range(n):
  homeworks.append(list(map(int, input().split())))

homeworks.sort(key = lambda x:x[1], reverse = True)

priority = [False] * (1001)
result = 0
for i in range(n):
  date, score = homeworks[i]
  d = date
  while d > 0 and priority[d]:
    d -= 1
  if d != 0:
    priority[d] = True
    result += score
    
print(result)

## priority = [False] * (n+1)로 하니 런타임에러가 남.. 왜 마감일이 n이하라고 착각했을까..? 마감일은 1000일 까지 가능함