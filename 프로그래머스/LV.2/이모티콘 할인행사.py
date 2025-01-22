from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    rates = [10, 20, 30, 40]
    emoticon_rate = list(product(rates, repeat = len(emoticons)))
    
    for er in emoticon_rate:
        count, money = 0, 0
        for i in range(len(users)):
            user_rate = users[i][0]
            
            total_price = 0
            for j in range(len(er)):
                if er[j] >= user_rate:
                    total_price += emoticons[j] * (100 - er[j]) * 0.01
                
            if total_price >= users[i][1]:
                count += 1
            else:
                money += total_price
                
        if answer[0] > count:
            continue
        
        if answer[0] == count and answer[1] > money:
            continue
            
        answer = [count, money]
    return answer
                
    
    
        
