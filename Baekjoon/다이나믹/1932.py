import sys

input = sys.stdin.readline
n = int(input())
floor = []

for _ in range(n):
    floor.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j==0:
            floor[i][j] += floor[i-1][j]
        elif j==i:
            floor[i][j] += floor[i-1][j-1]
        else:
            floor[i][j] += max(floor[i - 1][j - 1], floor[i - 1][j])
print(max(floor[n-1]))
