H, M = map(int,input().split())

if(M < 45):
    if(H==0):
        H=24
    M=(60+(M-45))
    H-=1
else:
    M-=45
print(H, M)