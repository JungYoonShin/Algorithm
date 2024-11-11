def solution(video_len, pos, op_start, op_end, commands):
    mm, ss = map(int, pos.split(":"))
    op_start_mm, op_start_ss = map(int, op_start.split(":"))
    op_end_mm, op_end_ss = map(int, op_end.split(":"))
    video_mm, video_ss = map(int, video_len.split(":"))
    
    
    for command in commands:
        # 오프닝 건너뛰기 조건
        if (op_start_ss + op_start_mm*60) <= (ss + mm*60) <= (op_end_ss + op_end_mm*60):
            mm = op_end_mm
            ss = op_end_ss

        if command == "next":
            if (video_ss + video_mm*60) - (ss + mm*60) <= 10:
                mm = video_mm
                ss = video_ss
            elif ss >= 50:
                mm += 1
                ss -= 50
            else:
                ss += 10

        elif command == "prev":
            if mm == 0 and ss <= 10:
                ss = 0
            elif ss < 10:
                mm -= 1
                ss += 50
            else:
                ss -= 10
                
    if (op_start_ss + op_start_mm*60) <= (ss + mm*60) <= (op_end_ss + op_end_mm*60):
        mm = op_end_mm
        ss = op_end_ss
            
    return str(mm).zfill(2)+":"+str(ss).zfill(2)
