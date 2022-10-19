import math

def solution(progresses, speeds):
    day = []
    answer = []
    cnt = 0
    
    for idx in range(len(progresses)):
        day.append(math.ceil((100 - progresses[idx]) / speeds[idx]))

    for i in day:
        print(answer)
        if i > cnt:
            answer.append(1)
            cnt = i
        else:
            answer[-1] += 1

    return answer