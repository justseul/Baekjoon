n, m = map(int,input().split())
answer = []
for i in range(n):
    arr = list(map(int,input().split()))
    answer.append(min(arr))

print(max(answer))