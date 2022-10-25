def solution(citations):
    i = max(citations)
    citations = sorted(citations, reverse=True)

    while(1): 
        if i <= list(map(lambda x : x >= i,citations)).count(1):
            return i
            
        i -=1
