from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for c in course:
        combi_count = defaultdict(int)
        
        for order in orders:
            for combi in combinations(sorted(order), c):
                combi_count[''.join(combi)] += 1
                
        
        if combi_count:
            max_cnt = max(combi_count.values())
            if max_cnt >= 2:
                for item, count in combi_count.items():
                    if count == max_cnt:
                        answer.append(item)

    return sorted(answer)
