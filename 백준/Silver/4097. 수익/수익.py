import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    best = -10**18
    cur = 0
    for _ in range(n):
        x = int(input())
        cur = max(x, cur + x)   
        best = max(best, cur)   

    print(best)
