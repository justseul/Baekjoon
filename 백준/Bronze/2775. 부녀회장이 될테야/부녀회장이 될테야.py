T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    apartment = [i for i in range(1, n+1)]

    for x in range(k):
        next = []
        for y in range(n):
            next.append(sum(apartment[:y+1]))
        apartment = next.copy()
    print(apartment[-1])