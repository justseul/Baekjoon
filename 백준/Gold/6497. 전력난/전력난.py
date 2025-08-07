import sys
import heapq
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    graph = [[] for _ in range(m)]
    chk = [0] * m
    total = 0
    answer = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        total += z
        graph[x].append((z, y))
        graph[y].append((z, x))

    heaq = [(0, 0)]

    while heaq:
        cost, node = heapq.heappop(heaq)
        if not chk[node]:
            chk[node] = 1
            answer += cost
            for edge in graph[node]:
                if not chk[edge[1]]:
                    heapq.heappush(heaq, edge)

    print(total - answer)
