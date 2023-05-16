N = int(input())
l = []
for i in range(N):
    w, h = map(int,input().split())
    l.append((w, h))

result = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            cnt += 1
    result.append(cnt+1)

for i in result:
    print(i, end =" ")