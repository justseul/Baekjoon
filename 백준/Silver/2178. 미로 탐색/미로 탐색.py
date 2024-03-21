def bfs(x, y):
    b_list = []
    b_list.append((x, y))
    while b_list:
        x, y = b_list.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                b_list.append((nx, ny))
    return graph[n-1][m-1]        
        

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(bfs(0,0))

