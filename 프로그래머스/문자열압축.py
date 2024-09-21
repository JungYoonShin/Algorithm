def solution(s):
  n = len(s)
  answer = len(s)
  for i in range(1, n//2+1):
      str_list = ''
      prev = s[0:i]
      cnt = 1
      for j in range(i, n, i):
          if prev == s[j:j+i]:
              cnt += 1
          else:
              str_list += str(cnt) + prev if cnt >= 2 else prev
              prev = s[j:j+i]
              cnt = 1
      str_list += str(cnt) + prev if cnt >= 2 else prev
      answer = min(answer, len(str_list))
  return answer
