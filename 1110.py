cycle = 0
n = int(input())
result = n
while(1):
    cycle = cycle + 1
    new = ((n%10)*10)+((n%10+n//10)%10)
    n = new
    if (new == result):
        break
print(cycle)
