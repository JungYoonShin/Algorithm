N=int(input())
A=list(map(int,input().split()))
M=max(A)
sum=0
for i in A:
    i=i/M*100
    sum+=i
average=sum/N
print(average)

