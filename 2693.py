x = int(input())
for i in range(x):
    num = list(map(int, input().split()))
    num.sort()
    print(num[-3])
