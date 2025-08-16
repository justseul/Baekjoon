import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
cost = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b] , c)

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
             if cost[j][i] > cost[j][k] + cost[k][i]:
                 cost[j][i] = cost[j][k] + cost[k][i]

for j in range(1, n+1):
    for i in range(1, n+1):
        if cost[j][i] == INF:
            print(0, end=' ')
        else: print(cost[j][i], end =' ')
    print()
