# https://www.acmicpc.net/problem/2439

#밀린만큼 빈칸 만들기 " "*(T-1)
T = int(input())

for i in range(1, T+1):
    print(" "*(T-i)+'*'*i)
