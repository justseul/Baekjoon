def solution(brown, yellow):    
    for i in range(1,yellow+1):
        if yellow % i == 0:
            w = i
            h = yellow // i
            if (w+h)*2 +4 == brown:
                return [h+2,w+2]