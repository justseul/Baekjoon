import sys
input = sys.stdin.readline

n = int(input())
a = [float(input()) for _ in range(n)]

dp = [0.0] * n
dp[0] = a[0]
ans = dp[0]

for i in range(1, n):
    dp[i] = max(a[i], dp[i-1] * a[i])
    if dp[i] > ans:
        ans = dp[i]

print(f"{ans:.3f}")
