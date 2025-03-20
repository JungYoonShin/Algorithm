from collections import defaultdict
def solution(gems):
    answer = []
    
    interval_sum = 0 #구간에 포함되는 보석 종류의 개수 
    n = len(gems)
    m = len(set(gems))
    start, end = 0, 0
    
    find_gem = defaultdict(int)
    min_len = 1e9
    
    for start in range(n):
        while len(find_gem) < m and end < n:
            find_gem[gems[end]] += 1
            end += 1
            
        if len(find_gem) == m:
            if end - start < min_len:
                min_len = end-start
                answer = [start+1, end]
        
        find_gem[gems[start]] -= 1
        if find_gem[gems[start]] == 0:
            del find_gem[gems[start]]
            
    return answer
