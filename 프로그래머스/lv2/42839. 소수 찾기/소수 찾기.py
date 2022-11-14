from itertools import permutations

def solution(numbers):
    dic = {}
    cnt = 0
    
    for i in range(1,len(list(numbers))+1):
        for j in list(permutations(numbers, i)):
            dic[int("".join(j))] = i

    for i in list(dic.keys()):
        state = True
        if(i<=1):
            continue
        else:
            for j in range(2,i//2+1):
                if(i%j==0):
                    state = False
            if(state == True):
                cnt += 1
    return cnt