from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

def bfs(N):
    visited = [False] * (N + 1)
    q = deque()
    q.append((N, 0)) 
    visited[N] = True

    while q:
        x, d = q.popleft()
        if x == 1:
            return d

        nx = x - 1
        if nx >= 1 and not visited[nx]:
            visited[nx] = True
            q.append((nx, d + 1))

        if x % 2 == 0:
            nx = x // 2
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, d + 1))

        if x % 3 == 0:
            nx = x // 3
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, d + 1))

print(bfs(N))