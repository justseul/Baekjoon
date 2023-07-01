n = int(input())
l = []
i = 1
c = True
b = []
for _ in range(n):
    a = int(input())
    while i <= a:
        l.append(i)
        i += 1
        b.append('+')  
        
    if l[-1] == a:
        l.pop()
        b.append('-')
    else:
        c = False
        break

if c == False:
    print('NO')
else:
    for i in b:
        print(i)