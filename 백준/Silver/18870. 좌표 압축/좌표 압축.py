n = int(input())
c = list(map(int,input().split()))
c_1 = set(c)
dic = {}
for i, n in enumerate(sorted(c_1)):
    dic[n] = i

for i in range(len(c)):
    if i == c[-1]:
        print(dic[c[i]])
    
    print(dic[c[i]], end=" ")
