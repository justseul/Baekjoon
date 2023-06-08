n = int(input())
m = int(input())
sosu = []
for i in range(n, m+1):
    cnt=0
    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        sosu.append(i)
if len(sosu) >= 1:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
