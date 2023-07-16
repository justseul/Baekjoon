person = []
for i in range(9):
    person.append(int(input()))

person.sort()

s = sum(person)

for i in range(len(person)):
    for j in range(i + 1, len(person)):
        if s - person[i] - person[j] == 100:
            for z in range(len(person)):
                if z == i or z == j:
                    pass
                else:
                    print(person[z])
            exit()
                    