while(1):
    list = []
    a,b,c = map(int,input().split())
    if a ==0 and b==0 and c==0:
        break
    list.append(a)
    list.append(b)
    list.append(c)
    if max(list) >= sum(list)-max(list):
        print('Invalid')
    else:
        
        list = set(list)
        if len(list)==1:
            print('Equilateral')
        elif len(list)==2:
            print('Isosceles')
        elif len(list)==3:
            print('Scalene')
        
