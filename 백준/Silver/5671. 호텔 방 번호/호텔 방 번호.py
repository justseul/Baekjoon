import sys
input = sys.stdin.readline

cnt = 0
try:
    while True:
        line = input().split()
        if not line:  
            break
        n, m = map(int, line)
        cnt = 0
        for i in range(n, m + 1):
            s = str(i)
            if len(set(s)) == len(s):  
                cnt += 1
        print(cnt)
except EOFError:
    pass