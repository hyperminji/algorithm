# https://www.acmicpc.net/problem/2675 

N = int(input())

for i in range(N):
    P,S = input().split()
    for j in range(len(S)):
        print(S[j]*int(P), end='') #공백없이
    print()#줄바꿈
