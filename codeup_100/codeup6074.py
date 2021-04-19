# 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
# https://www.codeup.kr/problem.php?id=6074
ch=input()
ch=ord(ch)
n=ord('a')
while n<=ch:
    print(chr(n),end=' ')
    n= n+1