# 12782번
n = int(input())

for _ in range(n):
    a, b = input().split()
    count_1 = 0
    count_0 = 0
    sum = 0
    for i in range(len(a)):
        #교환
        if a[i] != b[i]:
            if b[i] == '1':
                count_1 += 1
            else:
                count_0 += 1
        if count_1 >= 1 and count_0 >= 1:
            sum += 1
            count_1 -= 1
            count_0 -= 1
    if count_0 > 0 or count_1 > 0:
        sum += count_0 + count_1
    print(sum)

# 3
# 1011 1100
# 100101 110100
# 00110100 10010111

#다른 풀이 방법(간단하지만, 생각해내는게 어렵다,,)
n = int(input())

for _ in range(n):
  a, b = input().split()
  count_1 = 0
  count_0 = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      if b[i] == '1':
        count_1 += 1
      else:
        count_0 += 1
  print(max(count_1, count_0))
    