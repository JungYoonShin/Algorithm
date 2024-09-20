n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
time = 0
for i in p:
  time += i
  result += time

print(result)

'''
n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
for i in range(n):
  time = sum(p[0:i+1])
  result += time

print(result)
'''