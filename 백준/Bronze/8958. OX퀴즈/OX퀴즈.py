N = int(input())

for i in range(N):
    OX = list(input())
    score = 1
    sum = 0
    for i in OX:
        if(i =='O'):
            sum += score
            score += 1
        else:
            score = 1
        
    print(sum)