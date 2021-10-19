# https://www.acmicpc.net/problem/5622

inputlist=input()

num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

time = 0

for i in inputlist:
    for idx, dial in enumerate(num):
        if i in dial:
            time = time +3 +idx
            
print(time)
