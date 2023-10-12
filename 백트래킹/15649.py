import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [0] * (n+1)
result = []

def backtracking(count):
  global result
  if count == m:
    print(*result)
    return
  for i in range(1, n+1):
    if map[i] == 0:
      map[i] = 1
      result.append(i)
      backtracking(count+1)
      result.pop()
      map[i] = 0
      
backtracking(0)

## result.pop()을 11번째 줄 뒤에 두니까 원하는 대로 출력이 안되었다...