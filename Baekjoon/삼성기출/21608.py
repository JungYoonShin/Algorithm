import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
love = defaultdict(list)
student = [[0] * n for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n**2):
    s = list(map(int, input().split()))
    love[s[0]] = s[1:]

for lv in love.keys():
    can = []

    for i in range(n):
        for j in range(n):
            #빈자리라면, 좋아하는 사람과 주위의 빈자리 개수 확인
            if student[i][j] == 0:
                like, empty = 0, 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if student[nx][ny] in love[lv]:
                            like += 1

                        if student[nx][ny] == 0:
                            empty += 1
                can.append((i, j, like, empty))

    can.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    student[can[0][0]][can[0][1]] = lv

a = [0, 1, 10, 100, 1000]
answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if student[nx][ny] in love[student[i][j]]:
                    cnt += 1

        answer += a[cnt]
print(answer)
