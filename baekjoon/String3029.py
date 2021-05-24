#https://www.acmicpc.net/problem/3029
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

now_time = h1*60*60 + m1*60 + s1
start_show = h2*60*60 + m2*60 + s2

if start_show > now_time:
    wait_time = start_show - now_time
else:
    wait_time = start_show-now_time+24*60*60

#wait_time을 시간 형태로 표현
m, s = divmod(wait_time, 60)
h, m = divmod(m,60)

print("%02d:%02d:%02d" % (h, m, s))