import sys
n = list(sys.stdin.readline())
n = sorted(n,reverse = 1)
for i in range(len(n)-1):
    print(n[i], end="")



