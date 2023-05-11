import sys

input = sys.stdin.readline

bingo = dict()
check = [[0] * 5 for i in range(5)]

for i in range(5):
  num = list(map(int, input().split()))
  for j in range(5):
    bingo[num[j]] = (i, j)

cnt = 0
result = 0
for _ in range(5):
  MC = list(map(int, input().split()))
  for i in range(5):
    result += 1
    x, y = bingo[MC[i]]
    check[x][y] = 1

    cnt = 0
    for j in range(5):
      # 가로 빙고 세기
      if sum(check[j]) == 5:
        cnt += 1
      # 세로 빙고 세기
      if sum([k[j] for k in check]) == 5:
        cnt += 1

    #대각선 빙고 세기
    if check[0][4] + check[1][3] + check[2][2] + check[3][1] + check[4][0] == 5:
      cnt += 1
    if check[0][0] + check[1][1] + check[2][2] + check[3][3] + check[4][4] == 5:
      cnt += 1

    if cnt >= 3:
      print(result)
      sys.exit()
