import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
bus = list(map(int, input().split()))
bus_queue = deque(bus)
bridge = deque([])

cnt = 0
while bus_queue or bridge:
    #트럭 이동거리 증가
    for bus in bridge:
        bus[1] += 1

    #도착한 트럭은 제거
    if bridge and bridge[0][1] == w:
        bridge.popleft()

    if bus_queue and (sum(b[0] for b in bridge) + bus_queue[0]) <= L and len(bridge) < w:
        bus = bus_queue.popleft()
        bridge.append([bus, 0])

    cnt += 1
print(cnt)
