def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0
    for i in range(n-1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while pickup > 0 or delivery > 0:
            delivery -= cap
            pickup -= cap
            
            answer += (i+1)*2
    return answer
