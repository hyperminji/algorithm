# https://www.acmicpc.net/problem/1316

#단어 갯수만큼 반복한다
#단어를 입력
#현재 위치의 알파벳과 다음 위치의 알파벳이 다르면
#지금 위치의 알파벳이 뒤로 똑같은 알파벳 있으면 총 단어의 개수에서 1을 뺌



n = int(input())

for _ in range(n):
    word = input()
    
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                n = n-1
                break
print(n)
