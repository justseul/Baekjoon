import sys

input = sys.stdin.readline
n, k = map(int, input().split())
temp = list(map(int, input().split()))
result = []
result.append(sum(temp[:k]))

for i in range(n-k):
    result.append(result[i]-temp[i]+temp[k+i])

print(max(result))
