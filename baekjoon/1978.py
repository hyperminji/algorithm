#N개의 수가 주어진다
#둘째줄에 숫자가 주어진다
#주어진 숫자 중 소수를 판별하고 그 개수를 출력한다.
#N은 100이하 수는 1000이하의 자연수
n = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    if num <= 1:
        continue
    p = True  #소수
    for i in range(2, num): #소수판별
        if num % i == 0:  #소수가 아닌경우
            p = False
            break
    if p:
        count += 1
print(count)
        
        
