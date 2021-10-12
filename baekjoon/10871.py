# https://www.acmicpc.net/problem/10871
N, X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    if X > A[i]:
        print(A[i],end=" ")
