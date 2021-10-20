# https://www.acmicpc.net/problem/2475

koinum = list(map(int, input().split()))
sum = 0
for i in range(len(koinum)):
    sum = sum + koinum[i]*koinum[i]
checknum = sum%10

print(checknum)
