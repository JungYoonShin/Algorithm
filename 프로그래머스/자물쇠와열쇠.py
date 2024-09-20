def solution(key, lock):
  m = len(key)
  n = len(lock)

  #(n*3) * (n*3) 크기의 중간에 자물쇠 재배치
  new_lock = [[0] * (n*3) for _ in range(n*3)]
  for i in range(n):
      for j in range(n):
          new_lock[i+n][j+n] = lock[i][j]

  #시계방향으로 90도 회전 후 오른쪽으로 1, 아래로 1이동
  for _ in range(4):
      key = rotation(key)
      for x in range(1, n*2):
          for y in range(1, n*2):
              for i in range(m):
                  for j in range(m):
                      new_lock[i+x][j+y] += key[i][j]
              if check_sum(new_lock) == True:
                  return True
              else:
                  for i in range(m):
                      for j in range(m):
                          new_lock[i+x][j+y] -= key[i][j]

  return False

def check_sum(new_lock):
  n = len(new_lock) // 3
  for i in range(n, n*2):
      for j in range(n, n*2):
          if new_lock[i][j] != 1:
              return False
  return True


def rotation(key):
  newKey = []
  m = len(key)
  for i in range(m):
      arr = []
      for j in range(m-1, -1, -1):
          arr.append(key[j][i])
      newKey.append(arr)
  return newKey





