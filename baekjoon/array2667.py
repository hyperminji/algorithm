# https://www.acmicpc.net/problem/2667
#첫번째 줄에는 총 단지수를 출력
# 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오
# 총단지수
#첫번째 단지의 집수
#두번째 단지의 집수
#...


#단지수구하기
#단지의 집의 수 구하기

#1인 값을 찾는다 -> bfs로 0으로 바꿔준다(방문했으므로)-> count(집의 수)증가시켜 저장한다
#단지 수에 집의 수를 추가한다.

# 한 덩어리 찾고 거기서 몇집인지 세고, 다음 덩이리 찾고 거기서 몇집인지 센다 


# 집 하나씩 검사한다// 0이 나오는 경우 pass, 1인경우 상하좌우 모든집 구하기 
#bfs로 인접 노드의 모든 집을 구한다
#queue의 앞부터 pop-> visited, 단지 리스트에 추가한다
#상하좌우에 집이 있고 단지와 queue에 없다면 queue에 추가 
#queue가 빌때까지 계속 한다
#단지의 길이와 visited를return한다
# 요구한 대로 출력한다.

n = int(input())
hmap =[]
visited =[[0]*n for _ in range(n)]

for i in range(n):
    hmap.append(list(map(int, input())))
    
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x,y,c):
    visited[x][y] = 1
    global number
    if hmap[x][y]== 1:
        number = number+1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and hmap[nx][ny] == 1:
                dfs(nx, ny,c)

village =1
numlist = []
number = 0
for a in range(n):
    for b in range(n):
        if hmap[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b, village)
            numlist.append(number)
            number = 0
            
print(len(numlist))

for n in sorted(numlist):
    print(n)
    
