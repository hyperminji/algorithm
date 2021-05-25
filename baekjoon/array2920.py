#https://www.acmicpc.net/problem/2920

# 순서대로 -> ascending
# 반대로 ->  descending
#둘 다 아니면 -> mixed

#숫자를 입력 받는다
#if ifelse else돌린다.
a = list(map(int,input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')