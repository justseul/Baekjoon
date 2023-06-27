n = int(input())
l = []
for i in range(n):
    l.append(input())
l = set(l)

for x in sorted(l, key = lambda x: (len(x),x)):
    print(x)


    