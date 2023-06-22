import sys
input = sys.stdin.readline

n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n)]
timetable.sort(key =lambda x : (x[1], x[0]))

result = 0
end = 0
for start, now_end in timetable:
  if end <= start:
    end = now_end
    result +=1
print(result)