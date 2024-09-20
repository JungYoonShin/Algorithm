n, k = list(map(int, input().split()))
coin = []

for i in range(n):
  coin.append(int(input()))

result = 0
for i in range(n-1, -1, -1):
  result += k // coin[i]
  k %= coin[i]
  
print(result)