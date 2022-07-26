list1 = []

for i in range(10):
    A = int(input())
    B = A % 42
    list1.append(B)

list2 = set(list1)
print(len(list2))