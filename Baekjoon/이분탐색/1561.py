import sys

input = sys.stdin.readline

n, m = map(int, input().split())

times = list(map(int, input().split()))

left, right = 0, max(times) * n
while left <= right:
    mid = (left + right) // 2  #mid-> 모든 사람을 태우기 위한 최소 시간
    people = m

    for time in times:
        people += mid // time

    # n명 이상을 태울 수 있을 경우
    if people >= n:
        t = mid
        right = mid - 1
    else:
        left = mid + 1

# (t-1)시간 동안 태운 사람 수
people = m
for time in times:
    people += (t-1) // time

for i in range(m):
    if t % times[i] == 0:
        people += 1
    if people == n:
        print(i+1)
        break
