def solution(friends, gifts):
    n = len(friends)
    give_take = [[0 for _ in range(n)] for _ in range(n)]
    
    friends_dict = {}
    
    for i in range(n):
        friends_dict[friends[i]] = i
    
    # 주고 받은 선물
    for i in gifts:
        a, b = i.split(' ')
        give_take[friends_dict[a]][friends_dict[b]] += 1
        
    # 선물 지수
    graph = [[0 for _ in range(2)] for _ in range(n)]
    for i in range(n):
        graph[i][0] = sum(give_take[i])  # 준 선물 수
        
    for i in range(n):
        s = 0
        for j in range(n):
            s += give_take[j][i]  # 받은 선물 수
        graph[i][1] = s
    
    result = [0 for _ in range(n)]
        
    for i in range(n):
        for j in range(i+1, n):
            # 주고받은 이력x
            if give_take[i][j] == 0 and give_take[j][i] == 0:
                # 선물 지수 비교
                if graph[i][0] - graph[i][1] > graph[j][0] - graph[j][1]:
                    result[i] += 1
                elif graph[i][0] - graph[i][1] < graph[j][0] - graph[j][1]:
                    result[j] += 1
            
            # 주고받은 이력o
            else:
                if give_take[i][j] > give_take[j][i]:
                    result[i] += 1
                elif give_take[i][j] < give_take[j][i]:
                    result[j] += 1
                else:  # 주고받은 횟수가 같은 경우
                    # 선물 지수를 비교
                    if graph[i][0] - graph[i][1] > graph[j][0] - graph[j][1]:
                        result[i] += 1
                    elif graph[i][0] - graph[i][1] < graph[j][0] - graph[j][1]:
                        result[j] += 1
    
    return max(result)
