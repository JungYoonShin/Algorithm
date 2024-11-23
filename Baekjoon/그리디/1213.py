import sys
input = sys.stdin.readline

s = list(map(str, input().strip()))
s.sort()
counts = {}
count = []

for i in s:
    if i not in counts.keys():
        counts[i] = 1
    else:
        counts[i] += 1

for i in counts.keys():
    count.append([i, counts[i]])

count.sort()

result = ""
odd = ""
for i in count:
    if i[1] % 2 != 0:
        odd += i[0]
        s.remove(i[0])


if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    for i in range(0, len(s), 2):
        result += s[i]

    print(result + odd + result[::-1])
