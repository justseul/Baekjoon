import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

factory = [ [list(map(int, input().split())) for _ in range(n)] for _ in range(h) ]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if factory[z][x][y] == 1:
                q.append((z, x, y))

while q:
    z, x, y = q.popleft()
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if factory[nz][nx][ny] == 0:  
                factory[nz][nx][ny] = factory[z][x][y] + 1
                q.append((nz, nx, ny))

ans = 0
impossible = False 
for z in range(h):
    for x in range(n):
        for y in range(m):
            if factory[z][x][y] == 0:  
                impossible = True
            ans = max(ans, factory[z][x][y])
if impossible:
    print(-1)
else:
    print(ans - 1)
