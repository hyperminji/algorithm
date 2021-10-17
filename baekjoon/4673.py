# https://www.acmicpc.net/problem/4673

#d(75)= 75+7+5= 87
만개 = set(range(1,10001)) # set으로 중복 제거
생성자있는숫자 = set() # set으로 중복 제거

for i in range(1,10001):   # i = 987
    for  j in str(i):      # j = '9','8','7'
        i = i + int(j)     # 987+9+8+7  i = 1011
    생성자있는숫자.add(i)
셀프넘버 = sorted(만개 - 생성자있는숫자)
for i in 셀프넘버:
    print(i)
