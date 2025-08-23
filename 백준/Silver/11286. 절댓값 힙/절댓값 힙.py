import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
