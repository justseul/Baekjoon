l = []
a,b,c = map(int,input().split())

l.append(a)
l.append(b)
l.append(c)

while(1):
    if max(l) >= sum(l)-max(l):
        l[l.index(max(l))] -= 1
    else:
        print(sum(l))
        break
    