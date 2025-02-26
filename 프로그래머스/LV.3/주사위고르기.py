from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    for i in dice:
        i.sort()
    
    # 가능한 주사위 조합 
    combi = list(combinations(range(len(dice)), len(dice) // 2))
    not_combi = [tuple(set(range(len(dice))) - set(c)) for c in combi]
    
    result = {}
    for i in range(len(combi)):
        case = combi[i]
        n_case = not_combi[i]
        
        dices = [dice[temp] for temp in case]
        a_score_list = [sum(i) for i in product(*dices)]
    
        n_dices = [dice[temp] for temp in n_case]
        b_score_list = [sum(i) for i in product(*n_dices)]
        b_score_list.sort()

        wins = sum(bisect_left(b_score_list, score) for score in a_score_list)
        
        result[wins] = case
    
    max_key = max(result.keys())

    return [x+1 for x in result[max_key]]
        
