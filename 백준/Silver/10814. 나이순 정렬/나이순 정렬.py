n = int(input())
l = []
for i in range(n):
    age, name = input().split()
    l.append([i, int(age), name])

for a,b,c in sorted(l, key = lambda x: (x[1],x[0])):
    print(b,c)