import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

#치킨집 위치 저장(처음에 치킨집 위치만 저장해서 풀려고 했다..)
chicken, house, map = [], [], []

for i in range(n):
  for j in range(n):
    if city[i][j] == 2:
      chicken.append((i, j))
    elif city[i][j] == 1:
      house.append((i, j))
#거리 탐색
result = 10 ** 20
def backtracking(i, count):
  global result
  #거리 계산(m개가 모이면)
  if count == m:
    distance_all = 0
    for x, y in house:
      distance = 10 ** 20
      for a, b in map:
        distance = min(distance, abs(x-a) + abs(y-b))
      distance_all += distance
    result = min(distance_all, result)
    return
  if i >= len(chicken):
    return
  map.append(chicken[i])
  backtracking(i+1, count+1)
  map.pop()
  backtracking(i+1, count)

backtracking(0, 0)
print(result)