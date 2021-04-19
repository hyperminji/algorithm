# 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
# https://www.codeup.kr/problem.php?id=6075
n= int(input())
first= n
while n>=0:
    print(first - n)
    n= n-1