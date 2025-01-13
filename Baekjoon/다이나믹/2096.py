import sys

input = sys.stdin.readline

n = int(input())
game = list(map(int, input().split()))
max_result , min_result = game.copy(), game.copy()

for _ in range(n-1):
    game = list(map(int, input().split()))
    max_result = [game[0] + max(max_result[0], max_result[1]), game[1] + max(max_result), game[2] + max(max_result[1], max_result[2])]
    min_result = [game[0] + min(min_result[0], min_result[1]), game[1] + min(min_result), game[2] + min(min_result[1], min_result[2])]

print(max(max_result), min(min_result))

