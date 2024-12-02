import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
new_num = sorted(num)


for i in num:
    for j in range(n):
        if i == new_num[j]:
            print(j, end=" ")
            new_num[j] = -1
            break
