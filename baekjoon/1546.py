# https://www.acmicpc.net/problem/1546

#input()/input().max * 100

sub_num = int(input())
sub = list(map(int, input().split()))
sub_best = max(sub)
new = [subject/(sub_best*100) for subject in sub]
new_avg = sum(new)/sub_num*10000
print(new_avg)
