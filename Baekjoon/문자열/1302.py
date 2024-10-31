import sys

input = sys.stdin.readline

n = int(input())
book = {}
for _ in range(n):
    k = input().strip()
    if not k in book.keys():
        book[k] = 1
    else:
        book[k] += 1

max = max(book.values())
result = []
for i in book.keys():
    if book[i] == max:
        result.append(i)

result = sorted(result)

print(result[0])
