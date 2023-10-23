import sys
from collections import deque
input = sys.stdin.readline

def rotate_right(i, d):
  if i > 4:
    return
  if graph[i][6] != graph[i-1][2]:
    rotate_right(i+1, -d)
    graph[i].rotate(-d)

def rotate_left(i, d):
  if i < 1:
    return
  if graph[i][2] != graph[i+1][6]:
    rotate_left(i-1, -d)
    graph[i].rotate(-d)

graph = [0] * (10^20)
for i in range(1, 5):
  graph[i] = deque((map(int, input().rstrip())))
rotate_num = int(input())
for _ in range(rotate_num):
  n, d = map(int, input().split())
  rotate_right(n+1, d)
  rotate_left(n-1, d)
  graph[n].rotate(d)
result = 0
for i in range(4):
  result += graph[i + 1][0] * (2**i)
print(result)