# https://www.acmicpc.net/problem/2908

#ab를 입력받고 split
#a, b 뒤집는다(a[::-1])
#비교해서 프린트
a,b = input().split()

a= int(a[::-1])
b= int(b[::-1])

if a>b :
    print(a)
else:
    print(b)
