classNumber = int(input())
sum = 0
count = 0
avg=0
for i in range(classNumber):
    sum = 0
    count = 0
    avg=0
    studentNumber = list(map(int, input().split()))

    for j in studentNumber[1:]:
        sum += j

    avg = sum/studentNumber[0]

    for z in studentNumber[1:]:
        if(z > avg):
            count+=1
    print(f"{(count/studentNumber[0])*100:.3f}%")