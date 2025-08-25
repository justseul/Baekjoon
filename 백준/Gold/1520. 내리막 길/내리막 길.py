import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cells = [(maps[i][j], i, j) for i in range(n) for j in range(m)]
cells.sort(reverse=True)

dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

for h, x, y in cells:
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] < maps[x][y]:
            dp[nx][ny] += dp[x][y]

print(dp[n-1][m-1])