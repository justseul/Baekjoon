import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
fact = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if fact[i][j][k] == 1:
                q.append((i,j,k))

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while q:
    ez, ey, ex = q.popleft()
    for i in range(6):
        nz = ez + dz[i]
        ny = ey + dy[i]
        nx = ex + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and fact[nz][ny][nx] == 0:
            fact[nz][ny][nx] = fact[ez][ey][ex] + 1
            q.append((nz,ny,nx))
def solve():
    day = 1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if fact[i][j][k] == 0:
                    return -1
                day = max(day, fact[i][j][k] )
    return day-1

print(solve())