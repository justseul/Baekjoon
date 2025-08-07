import sys
import heapq
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    country, plane = map(int, input().split())
    line = [[] for _ in range(country+1)]
    visited = [0] * (country+1)
    for i in range(plane):
        a, b = map(int, input().split())
        line[a].append(b)
        line[b].append(a)
    heap = [1]
    rs = 0

    while heap:
        next_country = heapq.heappop(heap)
        if not visited[next_country]:
            visited[next_country] = True
            rs += 1
            for next_plane in line[next_country]:
                if not visited[next_plane]:
                    heapq.heappush(heap, next_plane)
    print(rs-1)