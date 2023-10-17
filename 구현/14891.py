#[삼성 SW 역량 테스트 기출]
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
  right_rotate(num + 1, direction)
  left_rotate(num - 1, direction)
  graph[num].rotate(direction)
result = 0
for i in range(4):
  result += graph[i + 1][0] * (2**i)
print(result)

## 참고:https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-14891-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
