N=int(input())
for i in range (N):
    for j in range(N):
        if j <= i:
            print('*', end='')
    print()   