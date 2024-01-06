import sys

n, k = map(int,sys.stdin.readline().split())

y = [i for i in range(1,1+n)]
respond = []
idx = 0 
while(len(y) != 0):
    idx += k-1
    if len(y) <= idx:
        idx = idx % len(y)
    respond.append(str(y.pop(idx)))
print("<", ", ".join(respond), ">", sep="")