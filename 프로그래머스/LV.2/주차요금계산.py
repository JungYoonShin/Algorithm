import math
def solution(fees, records):
    answer = []
    
    car = {}
    for record in records:
        a = record.split(' ')
        if a[1] not in car.keys():
            car[a[1]] = [a[0]]
        else:
            car[a[1]].append(a[0])
            
    result = {}
    for c, c_list in car.items():
        sums = 0
        for i in range(0, len(c_list), 2):
            if i+1 == len(c_list):  # 출차 기록이 없는 경우
                sh, sm = map(int, c_list[i].split(':'))
                eh, em = 23, 59  # 23:59까지 주차했다고 가정
            else:
                sh, sm = map(int, c_list[i].split(':'))
                eh, em = map(int, c_list[i+1].split(':'))

            sums += (eh * 60 + em) - (sh * 60 + sm)

        if sums <= fees[0]:  # 기본 시간 이하라면 기본 요금 부과
            fee = fees[1]
        else:  # 기본 시간을 초과한 경우 추가 요금 계산
            fee = fees[1] + math.ceil((sums - fees[0]) / fees[2]) * fees[3]
        
        result[c] = fee
        
    answer = [result[key] for key in sorted(result.keys())]
    
    return answer
