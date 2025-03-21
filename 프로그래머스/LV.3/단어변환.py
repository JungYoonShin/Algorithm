answer = 1e9
def dfs(begin, target, s, words, visited):
    global answer
    if begin == target:
        answer = min(answer, s)
        return
    
    for i in range(len(words)):
        cnt = 0
        word = words[i]
        if not visited[i]:
            for j in range(len(word)):
                if word[j] != begin[j]:
                    cnt += 1
            if cnt == 1:
                visited[i]= True
                s+=1
                dfs(word, target, s, words, visited)
                visited[i]= False
            
    return

def solution(begin, target, words):
    global answer
    
    # answer = float('inf')  # 최소 횟수를 구하므로 무한대로 초기화
    visited = [False] * len(words)
    dfs(begin, target, 0, words, visited)
    
    return answer if answer != 1e9 else 0  # 변환할 수 없다면 0을 반환
