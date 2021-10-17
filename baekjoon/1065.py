# https://www.acmicpc.net/problem/1065

#n이 주어졌을 때 1보다 크거나 같고, n보다 작거나 같은 한수의 개수
#99까지는 모두 간격이 1이기 때문에 등차수열인 한수에 들어감
한수 = 0
num = int(input())

for i in range(1, num+1):
    nums = list(map(int, str(i)))
    if i < 100:
        한수 = 한수+1
    elif nums[0] - nums[1] == nums[1] - nums[2]:
            한수= 한수 +1
print(한수)
