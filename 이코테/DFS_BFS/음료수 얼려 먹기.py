n, m = map(int, input().split())

map = list(list(map(int, list(input()))) for i in range(n))
# 동서남북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt, x, y = 0, 0, 0

def dfs(x, y):
    map[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            dfs(i,j)
            cnt += 1

print(cnt)
