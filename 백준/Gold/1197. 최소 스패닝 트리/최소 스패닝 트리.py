import sys
import heapq
input = sys.stdin.readline

# MST: 최소 비용으로 모든 노드 연결된 트리
# Kruskal: 작은 것부터 연결
# Prim: 현재 연결 중 가장 작은 것
# heap: 가장 작은 것 비교하는 알고리즘 > 최대or최소 찾는 자료구조
# heap = [[비용,노드]]

v, e = map(int, input().split())
edge = [[] for i in range(v+1)]
checked = [0] *(v+1)
heap = [[0,1]]
result = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])
while heap:
    w, each_node = heapq.heappop(heap)
    if checked[each_node] == 0:
        checked[each_node] = 1
        result += w
        for next_edge in edge[each_node]:
            if checked[next_edge[1]] == 0:
                heapq.heappush(heap, next_edge)
print(result)


