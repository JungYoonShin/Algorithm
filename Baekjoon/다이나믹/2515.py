import sys

input = sys.stdin.readline

n, s = map(int, input().split())

draw = [[0, 0]]
for _ in range(n):
    draw.append(list(map(int, input().split())))

draw.sort()

dp = [0 for _ in range(n+1)]
draw_index = [0 for _ in range(n+1)] #i번째 그림 앞에 위치할 수 있는 가장 높은 그림의 위치 idx를 저장 

for i in range(1, n+1):
    draw_index[i] = draw_index[i-1] + 1
    while draw_index[i] < i:
        if draw[i][0] - draw[draw_index[i]][0] < s:
            break
        draw_index[i] += 1
    draw_index[i] -= 1

for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[draw_index[i]] + draw[i][1])

print(dp[n])
