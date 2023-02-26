N, M = map(int, input().split())

basket = []
for _ in range(N):
    basket.append(0)
    
for throw in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        basket[idx] = k

for p in basket:
    print(p, end=" ")
