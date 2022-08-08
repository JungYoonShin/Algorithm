#17413번
n = input()

result = []
ss = ""
flag = 0
for i in n:
    ss += i
    if i == '<':
        #태그 사이에 문자가 있을 때
        if ss != "<":
            ss = ss[len(ss) - 2::-1]
            result.append(''.join(ss))
        ss = ""
        ss += i
        flag = 1
    if i == '>':
        flag = 0
        result.append(ss)
        ss = ""
    #문자 처리
    if flag == 0 and i == ' ':
        ss = ss[len(ss) - 2::-1] + ss[len(ss) - 1]
        result.append(''.join(ss))
        ss = ""
#남은 문자열에 대한 처리
if ss != "":
    ss = ss[::-1]
    result.append(''.join(ss))
print(''.join(result))
