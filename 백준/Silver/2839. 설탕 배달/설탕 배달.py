n = int(input())
s_n = []

for x in range(n):
    for y in range(n):
        if 3*x + 5*y == n:
            s_n.append(x+y)
        if 3*x + 5*y > n:
            break
if len(s_n) == 0: print(-1)
else: print(min(s_n))
    