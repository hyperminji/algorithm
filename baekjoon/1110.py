# https://www.acmicpc.net/problem/1110

#십의자리 // (몫), 일의자리 %(나머지)

n = int(input())
result = n
cycle= 0
num = 0
next_num = 0
while True:
    num = n//10 + n%10
    next_num = (n%10)*10 + num%10
    cycle = cycle+1
    n = next_num
    if next_num == result:
        break
print(cycle)
