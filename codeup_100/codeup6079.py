# 6079 : [기초-종합] 언제까지 더해야 할까?(py)
# https://www.codeup.kr/problem.php?id=6079
# 숫자를 계속 더해 나갈 때 그 합이 입력한 정수(1~1000)보다 같거나 작을 대까지만 계속 더하는 프로그램을 작성해보자
sum = 0
i = 0
num = int(input())
while True:
    i = i+ 1
    sum = sum+ i
    if (sum>= num):
        print(i)
        break