# https://www.acmicpc.net/problem/2941

a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
words = input()

for i in a:
    words = words.replace(i,'*')
print(len(words))
