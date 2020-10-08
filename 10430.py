A=5
B=8
C=4

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

A,B,C=map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

A,B,C=map(int,input().split())
print(((A+B)%C),((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep='\n')



