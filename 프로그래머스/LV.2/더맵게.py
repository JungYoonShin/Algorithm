from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    
    while len(scoville) >= 2:
    
        a = heappop(scoville)
        
        if a >= K:
            break
            
        b = heappop(scoville)
        
        new = a + b * 2
        heappush(scoville, new)
        answer += 1
        
    if heappop(scoville) < K:
        return -1
    return answer
