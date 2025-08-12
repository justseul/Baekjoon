import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        ew, ev = heapq.heappop(heap)
        if dist[ev] < ew:
            continue
        for nw, nv in graph[ev]:
            if dist[nv] > ew + nw:
                dist[nv] = ew + nw
                heapq.heappush(heap, (dist[nv], nv))
    return dist

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))           
    reverse_graph[b].append((t, a))   

to_home = dijkstra(x, graph, n)
from_home = dijkstra(x, reverse_graph, n)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, from_home[i] + to_home[i])

print(answer)
