import sys

input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

minus = []
plus = []
for book in books:
  if book < 0:
    minus.append(book)
  else:
    plus.append(book)

#가장 먼 위치의 책은 맨 마지막에 제자리에 둔다.(0으로 돌아올 필요 없으므로)
location = []
for i in range(0, len(minus), m):
  location.append(abs(minus[i]))
  if i + m > len(minus):
    break

for i in range(len(plus) - 1, -1, -m):
  location.append(plus[i])
  if i - m < 0:
    break

location.sort(reverse=True)
result = location[0] + sum(location[1:]) * 2
print(result)

## 정답률이 높아서 풀었는데 이 문제도 그리 쉽지는 않았다,,, (그리디 + 정렬)
