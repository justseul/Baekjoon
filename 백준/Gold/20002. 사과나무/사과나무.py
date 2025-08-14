import sys
input = sys.stdin.readline

n = int(input())
orchard = [list(map(int, input().split())) for _ in range(n)]

ps = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        ps[i][j] = orchard[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

max_value = -10**18 

for k in range(1, n + 1):  
    for i in range(n - k + 1): 
        for j in range(n - k + 1):
            total = ps[i+k][j+k] - ps[i][j+k] - ps[i+k][j] + ps[i][j]
            if total > max_value:
                max_value = total

print(max_value)
