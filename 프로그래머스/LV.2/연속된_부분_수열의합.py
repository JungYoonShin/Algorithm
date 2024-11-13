def solution(sequence, k):
    answer = []
    
    n = len(sequence)
    sum = 0
    end = 0
    
    result = []
    
    
    for start in range(n):
        while sum < k and end < n:
            sum += sequence[end]
            end += 1
        
        if sum == k:
            result.append([start, end-1])
        
        sum -= sequence[start]
    
    result.sort(key = lambda x: x[1]- x[0])
    answer = result[0]
    
    return answer
