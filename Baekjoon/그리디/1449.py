n, l = map(int, input().split())
location = list(map(int, input().split()))

location.sort()
length = [[0, 0]]
count = 0
for i in range(n):
  if length[len(length) - 1][1] < location[i] + 0.5:
    length.append([location[i] - 0.5, location[i] - 0.5 + l])
    count += 1
    
print(count)