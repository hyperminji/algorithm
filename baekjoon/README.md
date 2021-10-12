### 2021-10-12 
<details>
<summary>1. if문 </summary>
<div markdown="1">

- [2884: 알람 시계](https://www.acmicpc.net/problem/2884) 
    
  
    ```python
    h,m = map(int,input().split( ))
    if m >= 45:
        print(h, m-45)
    elif h>0 and m < 45:
        print(h-1, m+15)
    else:
        print(23, m+15)
    ```
    
- [14681: 사분면 고르기](https://www.acmicpc.net/problem/14681)
    
    
    ```python
    x= int(input())
    y= int(input())
    
    #1사분면 + +
    if x>0 and y >0:
        print(1)
    #2사분면 - +
    elif x<0 and y>0:
        print(2)
    #3사분면 - -
    elif x<0 and y<0:
        print(3)
    #4사분면 + -
    else:
        print(4)
    ```
  </div>
</details>
  
<details>
<summary>2. for문 </summary>
<div markdown="1">
         
- [2739: 구구단](https://www.acmicpc.net/problem/2739) 
  
    
    ```python
    n = int(input())
    for i in range(1,10):
        print(n ,'*', i ,'=',n*i)
    ```
    
- [10950: A+B - 3](https://www.acmicpc.net/problem/10950)
    
       
    ```python
    n=int(input())
    for i in range(n):
        a,b = map(int,input().split())
        answer = a+b
        print(answer)
    ```
    
- [8393: 합](https://www.acmicpc.net/problem/8393)
 
    ```python
    n= int(input())
    result = 0
    for i in range(n+1):
        result = result+i
    print(result)
    ```
    
-  [15552: 빠른 A+B](https://www.acmicpc.net/problem/15552)   
   
    
    ```python
    import sys
    T= int(input())
    for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    
    --------
    import sys
    T= int(input())
    for i in range(T):
        line = sys.stdin.readline()
        a,b = map(int, line.split())
        print(a+b)
    ```
    
- [2742: 기찍 N](https://www.acmicpc.net/problem/2742)   
    
    
    ```python
    n = int(input())
    for i in range(n):
        print(i+1)
    ```
    
- [2742: 기찍 N](https://www.acmicpc.net/problem/2742)   
    
    
    ```python
    n = int(input())
    for i in range(n):
        print(n-i)
    ```
    
- [11021: A+B - 7](https://www.acmicpc.net/problem/11021)   
    
    
    ```python
    T= int(input())
    for i in range(1, T+1):
        a,b = map(int,input().split())
        print("Case #"+str(i)+":",a+b)
    ```
    
- [11022: A+B - 8](https://www.acmicpc.net/problem/11022)   
    
    
    ```python
    T = int(input())
    
    for i in range(1, T+1):
        a,b = map(int, input().split())
        print("Case #"+str(i)+":",a,"+",b,"=",a+b)
    ```
    
- [2438: 별 찍기 - 1](https://www.acmicpc.net/problem/2438)  
    
    
    ```python
    star = int(input())
    for i in range(1,star+1):
        print('*'*i)
    ```
    
- [2439: 별 찍기 - 2](https://www.acmicpc.net/problem/2439)  
    
    
    ```python
    #밀린만큼 빈칸 만들기 " "*(T-1)
    T = int(input())
    
    for i in range(1, T+1):
        print(" "*(T-i)+'*'*i)
    ```
    
- [10871: X보다 작은 수](https://www.acmicpc.net/problem/10871)  
    
    
    ```python
    N, X = map(int,input().split())
    A = list(map(int,input().split()))
    
    for i in range(N):
        if X > A[i]:
            print(A[i],end=" ")
    ``` 
  </div>
</details>
 
<details>
<summary>3. while문 </summary>
<div markdown="1">
  
  - [10952: A+B - 5](https://www.acmicpc.net/problem/10952)
  
    ```python
    while True:
        a,b = map(int, input().split())
        if a==0 and b == 0:
            break
        print(a+b)
    ```
    
- [10951: A+B - 4](https://www.acmicpc.net/problem/10951)   
        
    ```python
    #예외처리방법
    while True:
        try:
            a,b = map(int, input().split())
            print(a+b)
        except:
            break
    ```
    
- [1110: 더하기 사이클](https://www.acmicpc.net/problem/1110)  
    
    
    ```python
    #십의자리 // (몫), 일의자리 %(나머지)
    
    n = int(input())
    result = n
    cycle= 0
    num = 0
    next_num = 0
    while True:
        num = n//10 + n%10
        next_num = (n%10)*10 + num%10
        cycle = cycle+1
        n = next_num
        if next_num == result:
            break
    print(cycle)
    ```
    </div>
</details>
  
