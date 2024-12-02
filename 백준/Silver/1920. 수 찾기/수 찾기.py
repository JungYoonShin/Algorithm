import sys

input = sys.stdin.readline

n = int(input())
n_dict = {}
nums = list(map(int, input().split()))
for i in nums:
    n_dict[i] = True

m = int(input())
m_nums = list(map(int, input().split()))
for i in m_nums:
    if i in n_dict:
        print(1)
    else:
        print(0)