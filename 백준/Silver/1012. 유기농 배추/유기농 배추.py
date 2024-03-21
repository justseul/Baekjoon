def bfs(x, y, field):
    b_list = [(x, y)]
    field[x][y] = 0
    while b_list:
        x, y = b_list.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if field[nx][ny] == 1:
                b_list.append((nx, ny))
                field[nx][ny] = 0  # 방문한 배추의 위치를 0으로 변경
                

T = int(input())         
for _ in range(T):
    m, n, k = map(int, input().split())
    cnt = 0
    field = [[0] * n for _ in range(m)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                bfs(i, j, field)
                cnt += 1
    print(cnt)
