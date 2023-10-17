import sys
from collections import deque

input = sys.stdin.readline


def right_rotate(num, direction):
  if num > 4:
    return
  if graph[num - 1][2] != graph[num][6]:
    right_rotate(num + 1, -direction)
    graph[num].rotate(-direction)


def left_rotate(num, direction):
  if num < 1:
    return
  if graph[num][2] != graph[num + 1][6]:
    left_rotate(num - 1, -direction)
    graph[num].rotate(-direction)


graph = [0] * (10 ^ 20)
for i in range(1, 5):
  graph[i] = deque((map(int, input().rstrip())))

rotate_num = int(input())
for _ in range(rotate_num):
  num, direction = map(int, input().split())
  right_rotate(num + 1,direction)
  left_rotate(num - 1, direction)
  graph[num].rotate(direction)
result = 0
for i in range(4):
  result += graph[i+1][0] * (2**i)
print(result)
