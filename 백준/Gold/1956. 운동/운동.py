import sys
INF = sys.maxsize
input = sys.stdin.readline

v, e = map(int, input().split())
cycle = [[INF] * (v+1) for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    cycle[a][b] = c
for i in range(v+1):
    cycle[i][i] = 0

for k in range(1, v+1):
    for j in range(1, v+1):
        for i in range(1, v+1):
            if cycle[j][i] > cycle[j][k] + cycle[k][i]:
                cycle[j][i] = cycle[j][k] + cycle[k][i]

answer = INF
for j in range(1, v+1):
    for i in range(1, v+1):
        if i != j and answer > cycle[i][j] + cycle[j][i]:
            answer = cycle[i][j] + cycle[j][i]
if answer >= INF: print(-1)
else: print(answer)