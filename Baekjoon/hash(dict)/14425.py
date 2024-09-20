import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for _ in range(n):
  str = input().rstrip()
  dict[str] = 1
check = [input().rstrip() for _ in range(m)]

sum = 0
for str in check:
  if str in dict:
    sum += 1
print(sum)

##set을 사용하여 푸는 방법
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# s = set([input() for _ in range(N)])
# cnt = 0
# for _ in range(M):
#     t = input()
#     if t in s:
#         cnt += 1
# print(cnt)