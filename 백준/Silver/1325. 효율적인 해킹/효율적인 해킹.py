import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
computer = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    computer[b].append(a)

def bfs(x):
    chk = [0] * (n + 1)
    cnt = 1
    q = deque([x])
    chk[x] = 1
    while q:
        n_com = q.popleft()
        for i in computer[n_com]:
            if chk[i] == 0:
                q.append(i)
                chk[i] = 1
                cnt += 1
    return cnt

answer = []
max_cnt = 0
for i in range(1,n+1):
        answer.append((bfs(i),i))
        if answer[i-1][0] > max_cnt:
            max_cnt = answer[i-1][0]

for i, idx in answer:
    if max_cnt == i:
        print(idx, end=' ')