def solution(survey, choices):
    answer = ''
    
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        ss = survey[i]
        # 동의 
        if choices[i] >= 5:
            dic[ss[1]] += choices[i] - 4
        
        # 비동의
        elif choices[i] < 4:
            dic[ss[0]] += 4 - choices[i]
            
    result = list(x for x in dic.items())
    for i in range(0, len(result), 2):
        if result[i][1] >= result[i+1][1]:
            answer += result[i][0]
        else:
            answer += result[i+1][0]
    return answer
        
