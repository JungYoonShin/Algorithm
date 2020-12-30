N,X=map(int,input().split())
A=list(map(int,input().split()))
for i in A:
    if i < X:
        print(i, end=' ')

N,X=map(int,input().split())
A=list(map(int,input().split()))
for i in range(len(A)):
    a=A[i]
    if a<X:
        print(a, end=' ')