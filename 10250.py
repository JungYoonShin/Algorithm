T = int(input())

def room_assignments(h, w, n):
    room = [[0] * 100 for _ in range(100)]     #2차원 배열 선언 및 0으로 초기
    count = 0
    for i in range(w):
        for j in range(h):
            count += 1
            if count == n:
                if i < 9:
                    print('%d0%d' %(j+1, i+1))
                else:
                    print('%d%d' % (j + 1, i + 1))
for i in range(T):
    number_of_floors, numbers_of_rooms, nth_guest = map(int, input().split())
    room_assignments(number_of_floors, numbers_of_rooms, nth_guest)
