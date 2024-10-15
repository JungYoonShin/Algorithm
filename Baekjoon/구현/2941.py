import sys

input = sys.stdin.readline
word = input().rstrip()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alphabet:
    word = word.replace(i, 'a')

print(len(word))
