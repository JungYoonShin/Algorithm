##어렵다....
case = int(input())
for _ in range(case):
  n, m = list(map(int, input().split()))
  queue = list(map(int, input().split()))
  count = 0
  while True:
    max_num = max(queue)
    front = queue.pop(0)
    m -= 1

    #맨 앞에 있는 데이터가 중요도가 가장 높을 때
    if max_num == front:
      count += 1
      #내가 출력될 차례
      if m < 0:
        print(count)
        break
    else:
      queue.append(front)
      if m < 0:
        m = len(queue) - 1
        
      
  
