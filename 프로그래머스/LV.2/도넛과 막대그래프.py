def solution(edges):
    answer = [0, 0, 0, 0]
    
    graph = {}
    for x, y in edges:
        if not graph.get(x):
            graph[x] = [0, 0] #나가는 간선, 들어오는 간선
            
        if not graph.get(y):
            graph[y] = [0, 0]
        
        graph[x][0] += 1
        graph[y][1] += 1
    
    for key, cnt in graph.items():
        if cnt[0] >= 2 and cnt[1] == 0:
            answer[0] = key
        elif cnt[0] == 0 and cnt[1] > 0:
            answer[2] += 1
        elif cnt[1] >= 2 and cnt[0] >= 2:
            answer[3] += 1
            
    answer[1] = graph[answer[0]][0] - answer[2] - answer[3]
    return answer
