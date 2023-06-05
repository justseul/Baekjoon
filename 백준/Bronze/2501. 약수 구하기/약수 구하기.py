N, K = map(int, input().split())
cnt = 0
measure = []
for i in range(1, N+1):
    if N%i==0:
        measure.append(i)
if K > len(measure):
    print(0)
else:
    print(measure[K-1])