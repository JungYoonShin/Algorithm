import sys
input = sys.stdin.readline

maps = []
n, k = list(map(int, input().split()))
for i in range(1, n+1):
    maps.append(i)

result = []
result.append(maps[k-1])
del maps[k-1]
a = k - 1

while maps:
    result.append(maps[(a+k-1)%len(maps)])
    temp = len(maps)
    del maps[(a+k-1)%len(maps)]
    a = (a+k-1)%temp

print("<", end="")
print(*result, sep=", ", end="")
print(">")
