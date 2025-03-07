def solution(n, k):
    answer = 0
    word = ""
    while n:
        word = str(n%k) + word
        n //= k
        
    word = word.split('0')

    for i in word:
        if i == '' or int(i) < 2:
            continue
        
        i = int(i)
        
        flag = True
        for j in range(2, int(i**(1/2)+1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            answer += 1
    
    return answer
