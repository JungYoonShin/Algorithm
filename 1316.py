N = int(input())


def is_group(s):
    group_str = [0] * 10000
    cnt = 0
    res = s[0]
    for x in s:
        x = ord(x)
        group_str[x] += 1
        if (chr(x) != res and group_str[x] > 1):
            return 0
        res = chr(x)
    cnt += 1
    return cnt


cnt = 0
for i in range(N):
    s = input()
    cnt += is_group(s)
print(cnt)