def solution(name, yearning, photo):
    answer = []
    name_yearning = {}
    for i in range(len(name)):
        name_yearning[name[i]] = yearning[i]
        
    for people in photo:
        sum = 0
        for man in people:
            if man in name_yearning:
                sum += name_yearning[man]
        answer.append(sum)
    return answer
