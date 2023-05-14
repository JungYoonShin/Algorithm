import sys

input = sys.stdin.readline
king, dol, n = input().split()
kx, ky = ord(king[0]) - ord('A') + 1, int(king[1])
dx, dy = ord(dol[0]) - ord('A') + 1, int(dol[1])
n = int(n)

x = [1, -1, 0, 0, 1, -1, 1, -1]
y = [0, 0, -1, 1, 1, 1, -1, -1]
move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

for _ in range(n):
  m = input().rstrip()
  for i in range(len(move)):
    if m == move[i]:
      nkx = kx + x[i]
      nky = ky + y[i]
      if (nkx > 0 and nkx <= 8 and nky > 0 and nky <= 8):
        #킹과 돌이 같은 위치라면
        if nkx == dx and nky == dy:
          ndx = dx + x[i]
          ndy = dy + y[i]
          if (ndx > 0 and ndx <= 8 and ndy > 0 and ndy <= 8):
            dx, dy = ndx, ndy
            kx, ky = nkx, nky
        else:
          kx, ky = nkx, nky

print(chr(kx + ord('A') - 1) + str(ky))
print(chr(dx + ord('A') - 1) + str(dy))
