import sys

input = sys.stdin.readline

# 방향 정의 (→, ←, ↑, ↓)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, k = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(n)]
pieces = [] # 각 말의 (x, y, 방향) 정보 저장
board = [[[] for _ in range(n)] for _ in range(n)]


# 말 정보 저장
for i in range(k):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    pieces.append([x, y, d])  # (x좌표, y좌표, 방향)
    board[x][y].append(i)  # 해당 좌표에 말 번호 저장

turn = 0  # 게임 턴 수

while turn <= 1000:
    turn += 1  # 턴 증가

    for i in range(k):
        x, y, d = pieces[i]  # 현재 말 위치 및 방향

        # 현재 말이 어디 있는지 찾기
        idx = board[x][y].index(i)  # 몇 번째 말인지 확인
        move_stack = board[x][y][idx:]  # 해당 말과 위에 있는 말들
        board[x][y] = board[x][y][:idx]  # 이동할 말들을 기존 위치에서 제거

        # 이동할 위치 계산
        nx, ny = x + dx[d], y + dy[d]

        # 범위를 벗어나거나 파란색(2)일 경우 → 방향 반대로 변경 후 다시 이동
        if not (0 <= nx < n and 0 <= ny < n) or chess[nx][ny] == 2:
            if d in [0, 2]:
                d += 1
            elif d in [1, 3]:
                d -= 1

            pieces[i][2] = d  # 방향 업데이트
            nx, ny = x + dx[d], y + dy[d]

            # 다시 이동할 위치도 파란색이거나 범위를 벗어나면 이동 안 함
            if not (0 <= nx < n and 0 <= ny < n) or chess[nx][ny] == 2:
                board[x][y].extend(move_stack)  # 이동 취소, 원래 위치로 복귀
                continue

        if chess[nx][ny] == 0:
            board[nx][ny].extend(move_stack)
        elif chess[nx][ny] == 1:
            board[nx][ny].extend(move_stack[::-1])

        for m in move_stack:
            pieces[m][0], pieces[m][1] = nx, ny

        # 말이 4개 이상 쌓이면 종료
        if len(board[nx][ny]) >= 4:
            print(turn)
            exit()

# 1000턴 초과 시 -1 출력
print(-1)
