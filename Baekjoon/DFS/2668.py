import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * n
graph = []
answer = set()
for _ in range(n):
    graph.append(int(input()))

def dfs(first, second, num):
    first.add(num)
    second.add(graph[num-1])
    visited[num-1] = True
    if graph[num-1] in first:
        if first == second:
            answer.update(first)
            return
        return
    dfs(first, second, graph[num-1])


for i in range(1, n+1):
    dfs(set(), set(), i)

answer = sorted(answer)
print(len(answer))
for n in answer:
    print(n)

