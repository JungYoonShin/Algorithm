#2217번
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

result = []
for i in range(n):
    result.append(rope[i] * (i + 1))

result = max(result)
print(result)
