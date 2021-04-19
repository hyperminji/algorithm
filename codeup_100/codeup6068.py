# 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)
# https://www.codeup.kr/problem.php?id=6068
# 90 ~ 100 : A, 70 ~ 89 : B, 40 ~ 69 : C, 0 ~ 39 : D
n = int(input())
if n>=90:
    print('A')
else:
    if n>=70:
        print('B')
    else:
        if n>=40:
            print('C')
        else:
            print('D')