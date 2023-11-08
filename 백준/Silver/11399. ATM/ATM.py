n = int(input())
p = list(map(int,input().split()))

p = sorted(p)

sum1 = sum(p)
for i in range(len(p)):
    sum1 += sum(p[:i])

print(sum1)
