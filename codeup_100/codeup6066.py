# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)
https://www.codeup.kr/problem.php?id=6066
a,b,c = map(int, input().split())

s= [a,b,c]

for i in s:
    if i%2==0:
        print("even")
    else:
        print("odd")
