from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque(maxlen=cacheSize)
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if not city in q:
            q.append(city)
            answer += 5
        elif city in q:
            q.remove(city)
            q.append(city)
            answer += 1
            
    return answer
