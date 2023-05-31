n, m = map(int,input().split())
m1,m2 = [], []

for i in range(2*n):
    if i < n:
        m1.append(list(map(int,input().split())))
    else:
        m2.append(list(map(int,input().split())))

for row in range(n):
    for col in range(m):
        print(m1[row][col] + m2[row][col], end=' ')
    print()