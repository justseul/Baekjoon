N = int(input())
cnt = 0

for i in range(1, N+1):
    if i <= 99 : 
        cnt += 1
    else :
        n = list(map(int,str(i)))
       
        if int(n[0]) - int(n[1]) == int(n[1]) - int(n[2]): 
            cnt += 1

print(cnt)         