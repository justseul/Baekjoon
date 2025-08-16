import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
a, b, c = map(int, input().split())
m = int(input())
road = [[] for _ in range(n + 1)]

for _ in range(m):
    d, e, l = map(int, input().split())
    road[d].append((l, e))
    road[e].append((l, d))

def dijkstra(start):
    chk = [INF] * (n + 1)
    chk[start] = 0
    heap = [(0, start)]
    while heap:
        ec, ev = heapq.heappop(heap)
        if chk[ev] != ec:
            continue
        for nc, nv in road[ev]:
            if chk[nv] > ec + nc:
                chk[nv] = ec + nc
                heapq.heappush(heap, (ec+nc, nv))
    return chk

dist_a = dijkstra(a)
dist_b = dijkstra(b)
dist_c = dijkstra(c)

answer = []
for i in range(1, n+1):
    answer.append(min(dist_a[i], dist_b[i], dist_c[i]))

max_val = max(answer)
print(*[idx+1 for idx, val in enumerate(answer) if val == max_val])