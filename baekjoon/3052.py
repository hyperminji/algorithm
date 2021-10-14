# https://www.acmicpc.net/problem/3052

n= []
# 연달아서 입력받는 방법
for _ in range(10):
    #인풋받아서 연산-나누고 나머지를 모은다
    num = int(input())
    n.append(num%42)
    # 중복제거
n = set(n)
print(len(n))
