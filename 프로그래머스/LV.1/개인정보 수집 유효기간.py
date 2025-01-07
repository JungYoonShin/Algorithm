def solution(today, terms, privacies):
    answer = []
    
    term = {}
    for i in terms:
        a, b = i.split(' ')
        term[a] = int(b)

    
    cnt = 0
    for i in privacies:
        cnt += 1
        date, type = i.split(' ')
        year, month, day = date.split('.')
        
        year = int(year)
        month = int(month)
        day = int(day)
        
        year += term[type] // 12
        month += term[type] % 12
        if month > 12:
            month -= 12
            year += 1
        if int(day) == 1:
            day = 28
            month -= 1
        else:
            day -= 1
        
        if month < 10:
            month = "0" + str(month)
        if day < 10:
            day = "0" + str(day)
        
        ymd = int(str(year) + str(month) + str(day))
        
        if int(today.replace(".", "")) > ymd:
            print(today.replace(".", ""), ymd)
            answer.append(cnt)
            
        
    return answer
