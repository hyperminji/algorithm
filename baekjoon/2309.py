import sys
#키 입력받기
height_list=[]
for i in range(9):
    height_list.append(int(sys.stdin.readline()))
#키의 합 구하기
total = sum(height_list)
#가짜 난쟁이 판별
end = False
for i in range(8):
    for j in range(i+1, 9):
        if (height_list[i] + height_list[j] == total - 100):
            fake=[i,j]
            end=True
            break
    if(end):
        break
#인덱스 이용 가짜 난쟁이 삭제        
del height_list[fake[0]]
del height_list[fake[1]-1] # 하나 지우면 한자리씩 자리가 당겨지므로 -1해준다
#오름차순 정리
height_list.sort()
#원소 출력
for i in height_list:
    print(i)
