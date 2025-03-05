def search(num):
    if len(num) == 1 or '1' not in num or '0' not in num:
        return True
    
    mid = len(num) // 2
    if num[mid] == '0':
        return False
    return search(num[:mid]) and search(num[mid+1:])
    

def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = bin(num)[2:]
        for i in range(1, 50):
            if (2 ** i) - 1 >= len(bin_num):
                n = i
                break
        dummy = (2 ** n -1 ) - len(bin_num)
        bin_num = '0' * dummy + bin_num
        
        answer.append(1 if search(bin_num) else 0)
        
    
    return answer
