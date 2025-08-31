import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * len(numbers)
cnt = 0
for i in range(len(numbers)):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)
            cnt += 1
print(max(dp))