x, y, w, h = map(int, input().split())
num = [x, y, w-x, h-y]
min = num[0]
for i in range(1,4):
    if num[i] < min:
        min = num[i]
print(min)
