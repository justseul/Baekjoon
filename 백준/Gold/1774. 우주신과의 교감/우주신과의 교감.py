import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
coord = [()]
edge = [[] for _ in range(n+1)]
chk = [0] * (n+1)

def dist(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

for _ in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))

for i in range(1, n):
    for j in range(i+1, n+1):
        d = dist(coord[i], coord[j])
        edge[i].append([d, j])
        edge[j].append([d, i])

for _ in range(m):
    node1, node2 = map(int, input().split())
    edge[node1].append([0, node2])
    edge[node2].append([0, node1])

heap = []
heapq.heappush(heap, [0, 1])  

answer = 0
while heap:
    c, e = heapq.heappop(heap)
    if chk[e]:
        continue
    chk[e] = True
    answer += c
    for cost, nxt in edge[e]:
        if not chk[nxt]:
            heapq.heappush(heap, [cost, nxt])

print(f"{answer:.2f}")
