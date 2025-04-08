def solution(citations):
    citations.sort()
    h = 0
    for i in range(len(citations)+1):
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1
        if i <= cnt:
            h = i
    return h

# 예제2 : [3, 4] >> 출력값 : 2

        
            