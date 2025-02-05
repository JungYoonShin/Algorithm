import sys

input = sys.stdin.readline

n, a, k = map(int, input().split()) #n x n, 볼 개수, 이동 횟수
ball = [[[]for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(a):
    r, c, m, s, d = map(int, input().split())
    ball[r-1][c-1].append((m, s, d))


for _ in range(k):
    # 모든 공 이동
    new_ball = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(ball[i][j]) > 0:
                for b in ball[i][j]:
                    m, s, d = b
                    nx = (i + dx[d] * s) % n 
                    ny = (j + dy[d] * s) % n

                    new_ball[nx][ny].append((m, s, d))

    #2개이상 파이어볼 하나로 합치기
    for i in range(n):
        for j in range(n):
            if len(new_ball[i][j]) >= 2:
                sum_m, sum_s, cnt = 0, 0, 0
                cnt_odd, cnt_even = 0, 0
                for b in new_ball[i][j]:
                    m, s, d = b
                    sum_m += m
                    sum_s += s
                    cnt += 1
                    if d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1

                new_ball[i][j] = []
                if sum_m // 5 > 0:
                    if cnt_odd == cnt or cnt_even == cnt:
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 0))
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 2))
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 4))
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 6))
                    else:
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 1))
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 3))
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 5))
                        new_ball[i][j].append((sum_m // 5, sum_s // cnt, 7))

    ball = new_ball

result = 0
for i in range(n):
    for j in range(n):
        if len(ball[i][j]) > 0:
            for b in ball[i][j]:
                result += b[0]
print(result)
