def solution(s):
    result = 0
    
    same, different = 0, 0
    
    start = s[0]
    for i in range(0, len(s)):
        if s[i] == start:
            same += 1
        else:
            different += 1
        if same == different:
            if i+1 < len(s):
                start = s[i+1]
            result += 1
            same, different = 0, 0
        if same != different and i == len(s)-1:
            result += 1

        
    return result
