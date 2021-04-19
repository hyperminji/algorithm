# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)
# https://www.codeup.kr/problem.php?id=6067
#음수/짝수 A
#음수/홀수 B
#양수/짝수 C
#양수/음수 D

n =  int(input())
#음수 일때
if n<0:
    if n%2==0:
        print('A')
    else:
        print('B')
#양수 일때
else:
    if n%2==0:
        print('C')
    else:
        print('D')

