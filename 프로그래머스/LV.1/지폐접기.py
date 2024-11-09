def solution(wallet, bill):
    answer = 0
    
    wallet.sort()

    while True:
        bill.sort()
        
        if bill[0] <= wallet[0] and bill[0] <= wallet[1]:
            if bill[1] <= wallet[0] and bill[1] <= wallet[1]:
                break
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            break
        bill.sort(reverse=True)
        bill[0] = (bill[0] // 2)
        
        answer += 1
    return answer

