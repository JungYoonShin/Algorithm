import sys
input = sys.stdin.readline

n, k = map(int, input().split())

circle = []

for i in range(1, n+1):
    circle.append(i)

result = []
out = k - 1
result.append(circle.pop(out))

while circle:
    out = (out + k-1) % len(circle)
    result.append(circle.pop(out))

print(str(result).replace('[', '<').replace(']', '>'))
