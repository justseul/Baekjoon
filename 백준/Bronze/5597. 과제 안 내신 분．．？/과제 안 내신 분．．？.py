list_1 = []
for i in range(1,31):
    list_1.append(i)
    
for _ in range(28):
    n = int(input())
    list_1.remove(n)
    list_1.sort()
print(list_1[0],list_1[1])