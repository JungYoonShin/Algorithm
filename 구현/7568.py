n = int(input())
k = []
for i in range(n):
  k.append(list(map(int, input().split())))

result = []
for i in k:
  cnt = 1
  for j in k:
    if i[0] < j[0] and i[1] <j[1]:
      cnt += 1
  result.append(cnt)

# for i in result:
#   print(i)
print(*result)

  