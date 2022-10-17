def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt_p1 = 0
    cnt_p2 = 0
    cnt_p3 = 0
    if len(answers) < len(p1):
        pass
    elif(len(answers) % len(p1) == 0):
        p1 = p1*(len(answers)//len(p1))
    else: 
        p1 = p1*(len(answers)//len(p1)) + p1[:(len(answers) % len(p1))]

    if len(answers) < len(p2):
        pass
    elif(len(answers) % len(p2) == 0):
        p2 = p2*(len(answers)//len(p2))
    else: 
        p2 = p2*(len(answers)//len(p2)) + p2[:(len(answers) % len(p2))]

    if len(answers) < len(p3):
        pass
    elif(len(answers) % len(p3) == 0):
        p3 = p3*(len(answers)//len(p3))
    else: 
        p3 = p3*(len(answers)//len(p3)) + p3[:(len(answers) % len(p3))]

    for i in range(len(answers)):
        if answers[i] == p1[i]:
            cnt_p1 +=1
        if answers[i] == p2[i]:
            cnt_p2 +=1
        if answers[i] == p3[i]:
            cnt_p3 +=1

    if cnt_p1 == cnt_p2 == cnt_p3:
        answers = [1,2,3]
    elif max([cnt_p1,cnt_p2,cnt_p3]) == cnt_p1 & cnt_p1 == cnt_p2:
        answers = [1,2]
    elif max([cnt_p1,cnt_p2,cnt_p3]) == cnt_p1 & cnt_p1 == cnt_p3:
        answers = [1,3]
    elif max([cnt_p1,cnt_p2,cnt_p3]) == cnt_p2 & cnt_p2 == cnt_p3:
        answers = [2,3]
    elif max([cnt_p1,cnt_p2,cnt_p3]) == cnt_p1:
            answers = [1]
    elif max([cnt_p1,cnt_p2,cnt_p3]) == cnt_p2:
        answers = [2]
    elif max([cnt_p1,cnt_p2,cnt_p3]) == cnt_p3:
        answers = [3]

    return answers