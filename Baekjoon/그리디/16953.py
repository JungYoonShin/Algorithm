#A → B
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
#방법1)
import sys

f = sys.stdin.readline
a, b = map(int, f().split())

result = 1
while (a < b):
  if(b % 10 == 1):
    b //= 10
  elif(b % 2 == 0):
    b //= 2
  else:
    break
  result += 1
if a == b:
  print(result)
else:
  print(-1)
  
#방법2)
import sys

f = sys.stdin.readline
a, b = map(int, f().split())

result = 1
while (b!=a):
  temp = b
  if(b % 10 == 1):
    b //= 10
  elif(b % 2 == 0):
    b //= 2
  result += 1

  if(temp == b):
    print(-1)
    break
  
else:
  print(result)


#시간 초과 뜬 코드..
# import sys

# f = sys.stdin.readline
# a, b = map(int, f().split())

# result = 1
# while (b!=a):
#   if(b % 10 == 1):
#     b //= 10
#   elif(b % 2 == 0):
#     b //= 2
#   result += 1

#   if(b <= a and b != a):
#     print(-1)
#     break
  
# else:
#   print(result)
