# https://www.acmicpc.net/problem/8958

n= int(input())

for i in range(n):
    ox = input()
    score = 0
    total = 0
    for item in ox:
        if item =='O':
            score = score +1
        else:
            score = 0
        total = total +score
    print(total)
