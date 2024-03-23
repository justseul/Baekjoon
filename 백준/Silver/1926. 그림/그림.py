def bfs(x, y):
    b_list = [(x, y)]
    num = 0
    while(b_list):
        x, y = b_list.pop(0)
        num += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                paper[nx][ny] = 0
                b_list.append((nx,ny))
    area.append(num)

n, m = map(int, input().split())

paper = []; area = [];
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    paper.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            paper[i][j] = 0            
            bfs(i,j)
            cnt += 1
print(cnt)
if cnt == 0 : print(0) 
else : print(max(area))