def solution(diffs, times, limit):    
    start = 1
    end = max(diffs)
    answer = end
    
    while start <= end:
        level = (start+end)//2
        time = times[0]
        
        for i in range(1, len(diffs)):
            if diffs[i] > level:
                fail = diffs[i] - level
                time_curr = times[i]
                time_prev = times[i-1]
                
                time += (time_curr + time_prev) * fail + time_curr
            else:
                time += times[i]
                
        if time <= limit:
            end = level-1
            answer = level
            
        else:
            start = level + 1
                
    return answer
