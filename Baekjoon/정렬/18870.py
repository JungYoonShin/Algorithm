import sys
input = sys.stdin.readline

n = int(input())
dots = list(map(int, input().split()))

new_dots = list(sorted(set(dots)))
dots_to_dict = {new_dots[i] : i for i in range(len(new_dots))}

for i in dots:
  print(dots_to_dict[i], end=' ')


### 7/13/2023 혼자서 못 풀었다.. set과 dict같은 자료형에 대해 더 알 수 있던 계기가 됨.
