def solution(keymap, targets):
  answer = []

  alphabet = [5000] * 500

  for key in keymap:
      for i in range(len(key)):
          alphabet[ord(key[i])] = min(i+1, alphabet[ord(key[i])])

  for target in targets:
      cnt = 0
      for t in target:
          if alphabet[ord(t)] == 5000:
              cnt = -1
              break
          cnt += alphabet[ord(t)]

      answer.append(cnt)

  return answer
