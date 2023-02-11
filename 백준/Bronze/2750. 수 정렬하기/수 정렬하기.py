N = int(input())
l = []
for i in range(N):
    number = int(input())
    l.append(number)
l.sort()
for j in l:
    print(j)