n = int(input())
cnt = 1
c = 1

if(n == 1):
    print(1)
elif(n <=7):
    print(2)
else:
    while 1:
        c += 6 * cnt
        
        cnt += 1
        if(c >= n):
            break    
        
    print(cnt)