import sys

input = sys.stdin.readline

n, c = map(int, input().split())
homes = [int(input().rstrip()) for _ in range(n)]
homes.sort()

answer = 0


def binary_search(start, end):
  while start <= end:
    mid = (start + end) // 2
    current = homes[0]
    cnt = 2
    for i in range(1, n):
      if homes[i] - current >= mid:
        cnt += 1
        current = homes[i]
    if cnt > c:
      global answer
      start = mid + 1
      answer = mid
    else:
      end = mid - 1


start = 1
end = homes[-1] - homes[0]
binary_search(start, end)
print(answer)

###짱 어렵다... 나중에 꼭 다시 풀어보자!
