import sys

input = sys.stdin.readline
king, dol, n = map(int, input().split())
k = ord(king[0])
print(k)

x = [1, -1, 0, 0, 1, -1, 1, -1]
y = [0, 0, -1, 1, 1, -1, 1, -1]
move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

# for i in range(n):
#   m = input()
#   for i in range(len(move)):
#     if m == move[i]:
#       nx = x + x[i]
#       ny = y + y[i]
      