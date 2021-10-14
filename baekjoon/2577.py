# https://www.acmicpc.net/problem/2577

# input -> 연산 -> list, str처리하고 
# count를 for에 넣고 돌리자 0~9
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
a = int(input())
b = int(input())
c = int(input())
result = a*b*c
result = list(str(result))

for i in range(10):
    print(result.count(str(i)))
