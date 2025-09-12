import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
nums = [list(map(int, input().split()))for _ in range(n)]
answer = [row[:] for row in nums]

def make_path(n,m,s):
    path = []
    top = s
    left = s
    bottom = n-s-1
    right =  m-s-1

    for i in range(top, bottom):
        path.append((i, left))
    for i in range(left, right):
        path.append((bottom, i))
    for i in range(bottom, top, -1):
        path.append((i, right))
    for i in range(right, left, -1):
        path.append((top, i))
    return path, len(path)

layers = min(n,m) // 2
for i in range(layers):
    path, l = make_path(n,m,i)
    k = r % l
    val = [nums[a][b] for (a, b) in path]
    rot = val[-k:] + val[:-k]
    for idx, (a, b) in enumerate(path):
        answer[a][b] = rot[idx]

for row in answer:
    print(*row)