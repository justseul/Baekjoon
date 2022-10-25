cnt = 1
line = 1
mo = 1
ja = 1

N =int(input())

while(1):
    if(line == 1):
        if(N==cnt):
            break
        mo += 1
        line += 1
        cnt += 1
    elif(line % 2 == 0):
        ja += 1
        mo -= 1
        cnt += 1
        if(N==cnt):
            break
        if(mo == 1):
            line += 1
            ja = line
            mo = 1
            cnt+= 1
    else: 
        ja -= 1
        mo += 1
        cnt += 1
        if(N==cnt):
            break
        if(ja == 1):
            line += 1
            ja = 1
            mo = line
            cnt+= 1
    if(N==cnt):
            break
print("{}/{}".format(ja,mo))