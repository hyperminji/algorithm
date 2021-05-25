#https://www.acmicpc.net/problem/10809

#find()는 찾는 값이 없으면 -1 반환
#String 내장함수 ascii_lowercase : 소문자 알파벳
#for 문 돌면서 a가 소문자 알파벳에 있으면 그 자리번호를 출력, 없으면 -1, 첫번째 글자는 0번째 위치

import string

a= input()
for i in string.ascii_lowercase:
    print(a.find(i), end=" ")
