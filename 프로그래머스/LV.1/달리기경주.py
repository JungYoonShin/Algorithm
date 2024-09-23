def solution(players, callings):
    answer = players
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i

    for call in callings:
        location = dic[call]
        dic[answer[location]] = location-1
        dic[answer[location-1]] = location
        answer[location-1], answer[location] = answer[location], answer[location-1]

    return answer
