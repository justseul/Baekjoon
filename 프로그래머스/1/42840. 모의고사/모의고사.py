def solution(answers):
    n = len(answers)
    p1 = [1, 2, 3, 4, 5] *n
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]*n
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*n
    answer = [0,0,0]
    for i in range(n):
        if p1[i] == answers[i]:
            answer[0] += 1
        if p2[i] == answers[i]:
            answer[1] += 1
        if p3[i] == answers[i]:
            answer[2] += 1
    final = []
    for i in range(len(answer)):
        if max(answer) == answer[i]:
            final.append(i+1)        
    return final