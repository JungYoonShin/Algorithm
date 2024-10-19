import sys

input = sys.stdin.readline
r, c, k = map(int, input().split())
maps = []

for _ in range(3):
    maps.append(list(map(int, input().split())))

def lets_sort(maps, RC):
    max_len = -1

    result = []

    for map in maps:
        new_list = []
        real_list = []
        dict = {}
        for num in map:
            if num == 0:
                continue
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1

        max_len = max(max_len, len(dict.keys())*2)

        for key, value in dict.items():
            new_list.append([key, value])
        new_list.sort(key=lambda x:(x[1], x[0]))

        for i in new_list:
            real_list.append(i[0])
            real_list.append(i[1])

        real_list = real_list[:100]

        result.append(real_list)

    for i in range(len(result)):
        while len(result[i]) != max_len:
            result[i].append(0)

    return result if RC == "R" else list(zip(*result))


time = 0
while True:
    height = len(maps)
    width = len(maps[0])

    if time > 100:
        print(-1)
        break

    if r-1 < len(maps) and c-1 < len(maps[0]):
        if maps[r-1][c-1] == k:
            print(time)
            break

    if height >= width:
        maps = lets_sort(maps, "R")

    else:
        maps = lets_sort(list(zip(*maps)), "C")

    time += 1
