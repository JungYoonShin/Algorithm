import sys
import math

input = sys.stdin.readline

n = input().rstrip()

count = [0 for _ in range(10)]

for i in n:
    i = int(i)
    if i == 6 or i == 9:
        count[9] += 1
    else:
        count[i] += 1

if count[9] != 0:
    count[9] = math.ceil(count[9] / 2)
print(max(count))
