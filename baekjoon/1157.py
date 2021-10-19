#  https://www.acmicpc.net/problem/1157

#대소문자 구별하지 않는다
#입력받은 글자를 모두 대문자 혹은 모두 소문자로 변환
#중복을 제거해서 세어야하는 글자들을 추출 
#for문돌면서 글자별로 몇개 있나 추출
#max count가 중복이면 ?로 처리되게 설정
#해당 알파벳 출력은 대문자
단어= input().lower()
알파벳 = list(set(단어))
count_단어=[]

for i in 알파벳:
    count = 단어.count(i)
    count_단어.append(count)

if count_단어.count(max(count_단어)) >= 2:
    print("?")
else:
    print(알파벳[(count_단어.index(max(count_단어)))].upper())
