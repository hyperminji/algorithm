# https://www.acmicpc.net/problem/11720

#input
n=int(input())

numline = input()
numlist = []

for i in range(n):
    numlist.append(int(numline[i]))
    
answer = sum(numlist)
print(answer)
