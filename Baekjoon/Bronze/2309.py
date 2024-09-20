import sys

input = sys.stdin.readline

heights = []

def findNanjang():
  heights.sort()
  height_sum = sum(heights)
  find_sum = height_sum - 100
  i, j = 0, 8
  while 0 <= i < 9 and 0 <= j < 9:
    if heights[i] + heights[j] == find_sum:
      del heights[i]
      del heights[j]
      return
    elif heights[i] + heights[j] < find_sum:
      i += 1
    else:
      j -= 1

for i in range(9):
  heights.append(int(input()))

findNanjang()
print("hi")
heights.sort()
print(*heights)