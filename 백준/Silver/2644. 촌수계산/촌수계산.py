import sys
input = sys.stdin.readline
n = int(input())
m1, m2 = map(int, input().split())
m = int(input())
family = [list() for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
visited = [0 for _ in range(n+1)]
result = []

def dfs(x, cnt):
    global tmp
    visited[x] = 1
    if x == m2:
        tmp = 1
        print(cnt)
    for val in family[x]:
        if visited[val] == 0:
            dfs(val,cnt+1)

tmp = 0
dfs(m1,0)
if tmp == 0:
    print(-1)