import sys, math

input = sys.stdin.readline

MAX = 123456
prime = [True for _ in range(MAX * 2)]

def init():
  for i in range(2, math.sqrt(MAX) + 1):
    if prime[i]:
      for j in range(i*2, MAX+1, i):
        prime[i] = False

def find(n):
  cnt = 0
  for i in range(1, n+1):
    if prime[i]:
      cnt += 1
  return cnt

init()
while True:
  n = int(input())
  print(find(n))
  


