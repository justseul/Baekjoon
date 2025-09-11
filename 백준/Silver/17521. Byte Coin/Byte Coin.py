import sys
input = sys.stdin.readline

n, w = map(int, input().split())
price = [int(input()) for _ in range(n)]

cash = w
hold = 0

for i in range(n - 1):
    if price[i + 1] > price[i]:
        buy = cash // price[i]
        if buy > 0:
            cash -= buy * price[i]
            hold += buy

    elif price[i + 1] < price[i]:
        if hold > 0:
            cash += hold * price[i]
            hold = 0

if hold > 0:
    cash += hold * price[-1]

print(cash)
