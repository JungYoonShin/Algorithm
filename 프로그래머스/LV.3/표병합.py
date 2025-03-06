def solution(commands):
    answer = []
    
    cell = [["EMPTY"] * 51 for _ in range(51)]
    point = [[[i, j] for j in range(51)] for i in range(51)]

    for command in commands:
        a = command.split()
        
        if a[0] == 'UPDATE' and len(a) == 4:
            _, r, c, value = a
            r, c = int(r), int(c)
            rr, cc = point[r][c]
            cell[rr][cc] = value

        elif a[0] == 'UPDATE' and len(a) == 3:
            _, value1, value2 = a
            for i in range(51):
                for j in range(51):
                    if cell[i][j] == value1:
                        cell[i][j] = value2
            
        elif a[0] == 'MERGE':
            _, r1, c1, r2, c2 = a
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
            r_1, c_1 = point[r1][c1]
            r_2, c_2 = point[r2][c2]
            value1 = cell[r_1][c_1]
            value2 = cell[r_2][c_2]
            cell[r_1][c_1] = value2 if value1 == 'EMPTY' else value1
            
            for i in range(51):
                for j in range(51):
                    if point[i][j] == [r_2, c_2]:
                        point[i][j] = [r_1, c_1]
        
        elif a[0] == 'UNMERGE':
            _, r, c, = a
            r, c = int(r), int(c)
            rr, cc = point[r][c]
            value = cell[rr][cc]
            for i in range(51):
                for j in range(51):
                    if point[i][j] == [rr, cc]:
                        point[i][j] = [i, j]
                        cell[i][j] = 'EMPTY'
            cell[r][c] = value
        else:
            _, r, c = a
            r, c = int(r), int(c)
            rr, cc = point[r][c]
            answer.append(cell[rr][cc])
            
    return answer
