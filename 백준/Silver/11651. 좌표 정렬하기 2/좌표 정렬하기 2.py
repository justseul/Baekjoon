n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

for x, y in sorted(l, key = lambda x : (x[1],x[0])):
    print(x, y)


    