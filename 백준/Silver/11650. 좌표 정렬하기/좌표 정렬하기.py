n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

for x, y in sorted(l):
    print(x,y)
    