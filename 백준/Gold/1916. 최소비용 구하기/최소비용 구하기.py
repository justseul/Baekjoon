import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
maps = [[] for _ in range(n+1)]
cost = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((c, b))

start, end = map(int, input().split())
cost[start] = 0
heap = [(0, start)]

while heap:
    ew, ev = heapq.heappop(heap)
    if cost[ev] != ew: continue
    for nw, nv in maps[ev]:
        if cost[nv] > ew + nw:
            cost[nv] = ew + nw
            heapq.heappush(heap, (cost[nv], nv))
print(cost[end])