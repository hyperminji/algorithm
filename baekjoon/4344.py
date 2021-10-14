# https://www.acmicpc.net/problem/4344

#평균 구하기
#비교해서 평균보다 몇명 많나
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    count = 0
    for grade in nums[1:]:
        if grade > avg:
            count = count +1
    rate = (count/nums[0])*100
    print(f'{rate:.3f}%')
