#https://www.acmicpc.net/problem/2164


from collections import deque
n = int(input())
dqueue = deque(range(1, n+1))
while len(dqueue) > 1 :
    dqueue.popleft()
    dqueue.append(dqueue.popleft())

print(dqueue.pop())
