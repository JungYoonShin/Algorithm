from collections import defaultdict
import sys
input = sys.stdin.readline

n, p, q = list(map(int, input().split()))

dict = defaultdict(int)
def infinite(x):
  if x == 0:
    return 1
  if dict[x] != 0:
    return dict[x]
  dict[x] = infinite(x//p) + infinite(x//q)
  return dict[x]

print(infinite(n))

##defaultdict는 처음 써봤다,, dict는 key가 없어도 내부적으로 default값을 부여할 수 있다. 