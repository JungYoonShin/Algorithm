import sys

input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

min_level = 1e9
visited = [False] * n


def dfs(cnt, idx):
    global min_level, start

    if cnt == n // 2:
        link_sum = 0
        start_sum = 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start_sum += people[i][j]
                elif not visited[i] and not visited[j]:
                    link_sum += people[i][j]

        min_level = min(min_level, abs(start_sum-link_sum))
        return

    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(cnt + 1, i+1)
                visited[i] = False

dfs(0, 0)
print(min_level)
