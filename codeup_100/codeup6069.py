# 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)
#A : best!!! / B : good!! / C : run! / D : slowly~ / 나머지 문자들 : what?
grade = input()

if grade == 'A':
    print('best!!!')
else:
    if grade == 'B':
        print('good!!')
    else:
        if grade =='C':
            print('run!')
        else:
            if grade == 'D':
                print('slowly~')
            else:
                print('what?')