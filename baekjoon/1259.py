# https://www.acmicpc.net/problem/1259

while True:
    n = input()
    if n == '0':
        break   #빠져나가야 하니까 break사용
    if n[:] == n[::-1]:  # n뒤집을때 [:] 전체를  [범위:-1] 역순
        print("yes")
    else:
        print("no")

