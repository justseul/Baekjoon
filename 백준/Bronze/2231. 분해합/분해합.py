N = int(input())
i = 1
while(1):
    
    if sum(list(map(int, list(str(i))))) + i == N:  
        print(i)
        break
    elif i==N:
        print(0)
        break
    else:
        i+= 1
    
    