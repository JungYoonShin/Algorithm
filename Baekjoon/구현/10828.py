import sys

input = sys.stdin.readline
n = int(input())
stack1 = []
result = []


def stack(order):
  if order[0] == "push":
    stack1.append(int(order[1]))
  elif order[0] == "top":
    a = -1 if not stack1 else stack1[-1]
    result.append(a)
  elif order[0] == "pop":
    a = -1 if not stack1 else stack1.pop()
    result.append(a)
  elif order[0] == "size":
    result.append(len(stack1))
  else:
    a = 1 if not stack1 else 0
    result.append(a)


for _ in range(n):
  orders = input()
  order = orders.split()
  stack(order)
print(*result)

##삼항연산자, split(), join() 에 대해 다시 공부하게 됨
##empty의 경우 len(x)보다는 not x 로 확인하는게 더 좋다고 함