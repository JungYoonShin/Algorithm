a=int(input())
if (a%4==0 and a%100!=0) or a%400==0:
    print('1')
else:
    print('0')

year=int(input())
if ((year%4==0 and year%100!=0) or year%400==0):
    print(1)
else:
    print(0)
