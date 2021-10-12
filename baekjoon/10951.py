# https://www.acmicpc.net/problem/10951

#예외처리방법
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
