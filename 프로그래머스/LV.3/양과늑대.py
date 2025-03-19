def solution(info, edges):
    global answer
    answer = 0
    
    visited = [False] * len(info)
    
    def dfs(sheep, wolf):
        global answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return 
        
        for a, b in edges:
            if visited[a] and not visited[b]:
                visited[b]= True
                if info[b] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[b] = 0

    visited[0] = 1
    dfs(1, 0)
    
    return answer
