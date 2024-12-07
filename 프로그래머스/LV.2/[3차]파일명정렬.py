def solution(files):
    answer = []
    
    new_files = []
    for file in files:
        head = ""
        number = ""
        tail = ""
        flag = False
        for i in range(len(file)): # 문자열 자르기
            if file[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += file[i]
                flag = True
            elif not flag:  # NUMBER가 나오기 전까지는 HEAD
                head += file[i]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = file[i:]
                break
        new_files.append([head, number, tail])
    
    new_files.sort(key=lambda x: (x[0].upper(), (int(x[1]))))
    return [''.join(t) for t in new_files]  
