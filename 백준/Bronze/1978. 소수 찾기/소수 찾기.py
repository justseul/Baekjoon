n = int(input())
l1 = []

n1 = list(map(int,input().split()))
for n2 in n1:
    l = []
    for j in range(1,n2+1):
        if n2%j == 0:
            l.append(j)
    if len(l) == 2:
        l1.append(l)
print(len(l1))