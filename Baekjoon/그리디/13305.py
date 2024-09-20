import sys
input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = price[0] * distance[0]
low = price[0]

for i in range(1, N-1):
  if(price[i] < low):
    low = price[i]
  result += low * distance[i]
    
print(result)
