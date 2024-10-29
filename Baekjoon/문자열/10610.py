n = input()

if "0" not in n:
    print(-1)
else:
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0:
        n = sorted(n, reverse=True)
        for i in n:
            print(i, end="")
    else:
        print(-1)
