c=int(input())
sum=0
count=0
for i in range(c):
    N=list(map(int,input().split()))
    for j in range(1,len(N)):
        sum+=N[j]
    average=sum/j
    sum=0
    for k in range(1,len(N)):
        if(N[k]>average):
            count+=1
        else:
            continue
    print('{0:.3f}'.format(count / k * 100))
    # print('%0.3f' % round(count / k * 100, 3) + "%")
    count=0



