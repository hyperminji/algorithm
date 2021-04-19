# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
# https://www.codeup.kr/problem.php?id=6083
r,g,b = map(int, input().split())
num=0
for i in range(r):
    for j in range(g):
        for z in range(b):
            num = num+1
            print(i,j,z)
print(num)            