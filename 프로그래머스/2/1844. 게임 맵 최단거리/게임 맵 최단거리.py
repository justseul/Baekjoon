from collections import deque

def bfs(x, y, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
    
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1

def solution(maps):
    return bfs(0, 0, maps)