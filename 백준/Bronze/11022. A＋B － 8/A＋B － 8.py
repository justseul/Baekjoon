n = int(input())

for i in range(n):
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1,A,B,A+B))