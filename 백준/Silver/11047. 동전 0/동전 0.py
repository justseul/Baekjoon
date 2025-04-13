import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = list()
cnt = 0

for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

for j in coin:
    if j <= k :
        cnt += k // j
        k %= j
print(cnt) 
