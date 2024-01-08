n, m = map(int,input().split())

rs = []
chk = [False] * (n+1)

def rec(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return 
    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            rec(num+1)
            chk[i] = False
            rs.pop()
            
rec(0)
        
        
        
    