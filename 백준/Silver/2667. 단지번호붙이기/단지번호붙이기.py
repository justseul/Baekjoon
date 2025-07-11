import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for i in range(n)]

all_cnt = 0
answer = list()
cnt = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            DFS(nx, ny)
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            answer.append(DFS(i, j))

answer.sort()
print(len(answer))
print(*answer, sep="\n")
