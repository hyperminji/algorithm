# https://www.acmicpc.net/problem/15552
import sys
T= int(input())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

--------
import sys
T= int(input())
for i in range(T):
    line = sys.stdin.readline()
    a,b = map(int, line.split())
    print(a+b)
