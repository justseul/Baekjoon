def solution(n, lost, reserve):
    answer = n - len(lost)
    lost2 = []
    lost.sort()
    reserve.sort()
    
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
        else:
            lost2.append(i)
    lost = lost2

    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
            continue
        if i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
    return answer