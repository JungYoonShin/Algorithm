import sys

input = sys.stdin.readline
n = int(input())
for i in range(n-1):
  a, b = map(int, input().split())

graph = [[0] for _ in range(n)]
print(graph)