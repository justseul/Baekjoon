# 인접 그래프 만들기
#   비용, 연결 노드

import sys
import heapq
input = sys.stdin.readline

n = int(input())
star = [[] for _ in range(n+1)]
star_line = [[] for _ in range(n+1)]
chk = [0] * (n+1)

def cost(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

for i in range(1, n+1):
    x, y = map(float, input().split())
    star[i].append((x,y))

for i in range(1,n+1):
    for j in range(1, n + 1):
        if i != j:
            star_line[i].append((cost(*star[i][0], *star[j][0]), j))

heap = [[0,1]]
cost = 0
while(heap):
    c, next = heapq.heappop(heap)
    if not chk[next]:
        chk[next] = True
        cost += c
    for i in star_line[next]:
        if not chk[i[1]]:
            heapq.heappush(heap, i)

print(f"{cost:.2f}")
