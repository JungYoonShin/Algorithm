#입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
import sys
T=int(input())
for i in range (T):
    a,b= map(int,sys.stdin.readline().split())
    print(a+b)