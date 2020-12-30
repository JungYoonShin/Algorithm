self_number=[]
num=[]
for i in range(1,10001):
    self_number.append(i)
    for a in str(i):
        i=i+int(a)
    num.append(i)

self_number = [x for x in self_number if x not in num]
for i in self_number:
    print(i)