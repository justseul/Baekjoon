from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    
    def bfs(start):
        q = deque([start])
        visited = [0] * (n+1)
        visited[start] = 1
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if visited[i] == 0:
                    q.append(i)
                    cnt += 1
                    visited[i] = 1
                    
        return cnt
    res = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        res = min(abs(bfs(b)-bfs(a)), res)
        graph[a].append(b)
        graph[b].append(a)
            
    return res