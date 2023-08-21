import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

sum = [0] * (k+1)
sum[0] = 1 # 예를 들어 2원동전 1개만으로 2원을 만들때 필요

for coin in coins:
  #2원으로는 2원부터 만들 수 있음(2원을 무조건 포함함)
  for i in range(coin, k+1):
    sum[i] += sum[i-coin]

print(sum[k])
##다이나믹 프로그래밍은 점화식을 구하는 것이 중요, 예외를 생각하기보다 식을 세우는 것에 집중하는 것이 좋다고함
#참고 레퍼런스 : https://seongonion.tistory.com/108