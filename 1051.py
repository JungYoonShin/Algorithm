a, b = map(int,input().split())
num = [0] * a
li1 = [[0] * b for i in range(a)]
maxList = []
def findSquare(i):
    for j in range(b):
        for k in range(j+1, b):
            if(li1[i][j] == li1[i][k]):
                for p in range(i+1, a):
                    if(k-j+i)<a:
                        if(li1[k-j+i][j] == li1[i][j] and li1[k-j+i][k] == li1[i][k]):
                            maxList.append((k - j + 1) * (k - j + 1))

for i in range(a):
    num[i] = int(input())
    j = 0
    while True:
        r = num[i] % 10
        num[i] //= 10
        li1[i][j] = r
        j += 1
        if (num[i] == 0):
            break
for i in range(a):
    findSquare(i)

max = 0
for i in range(len(maxList)):
    if(maxList[i] > max):
        max = maxList[i]
if(max ==0):
    max = 1
print(max)
