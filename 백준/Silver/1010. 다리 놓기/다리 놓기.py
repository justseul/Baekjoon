import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(n+1)]

    for j in range(1, m+1):
        dp[1][j] = j  
        
    for i in range(2, n+1):
        for j in range(i, m+1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    print(dp[n][m])
