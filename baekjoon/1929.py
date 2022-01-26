#M에서 N사이의 소수 찾기
#하나씩 출력
def check_prime(num):
    if num ==1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num%n == 0:
                return False
        return True
M,N= map(int,input().split())
for i in range(M, N+1):
    if check_prime(i):
        print(i)
