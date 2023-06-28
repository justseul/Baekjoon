n = int(input())

for i in range(n):
    a = list(input().split())
    new_a = []
    for i in a:
        new_a.append(i[::-1])
    a = new_a[0]
    for i in range(1,len(new_a)):
        a += " " +new_a[i]

    print(a)