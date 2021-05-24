#https://www.acmicpc.net/problem/11720

#input
n=int(input())
#두번째 숫자열
numline = input()
numlist = []

for i in range(n):
    numlist.append(int(numline[i]))
    
answer = sum(numlist)
print(answer)