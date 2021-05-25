#https://www.acmicpc.net/submit/2953

#요리사=[[첫번째 점수들],[두번째 점수들],[세번째 점수들],[네번째 점수들]]--> 불필요함
#for문 돌려서 요리사[i]의 합을 구한다
#요리사 점수합계에 저장 
#max(요리사 점수합계),  요리사 점수합계.index(max(요리사 점수합계))+1 
sum_point=[]
for i in range(5):
    sum_point.append( sum(map(int,input().split())) )
print(sum_point.index(max(sum_point))+1, max(sum_point))
    

