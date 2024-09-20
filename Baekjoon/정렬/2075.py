import sys, heapq

input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
  nums = list(map(int, input().split()))
  for num in nums:
    if len(heap) < n:
      heapq.heappush(heap, num)
    #큐가 꽉 찬경우
    else:
      if heap[0] < num:
        heapq.heappop(heap)
        heapq.heappush(heap, num)
print(heap[0])
###heapq는 처음 알게 됨!! 블로그 참고해서 풀었음(그냥 정렬로 풀면 아마도 메모리 초과?)