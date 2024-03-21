def bfs(x, y):
    b_list = [(x, y)]
    maps[x][y] = 0
    cnt = 1
    while b_list:
        x, y = b_list.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                cnt += 1
                b_list.append((nx,ny))
                maps[nx][ny] = 0
    return cnt

        
complex = []
maps = []  # 변수 이름 변경
n = int(input())
for i in range(n):
    maps.append(list(map(int, input())))    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            complex.append(bfs(i,j))
print(len(complex))
for i in sorted(complex):
    print(i)