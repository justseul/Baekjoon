def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for i in range(n)]
    l = []
    l.append((0, 0))
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    while l:
        x, y = l.pop(0)
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    l.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1

    if visited[n-1][m-1] == 1:
        answer = maps[n-1][m-1]
        return answer
    else:
        return -1