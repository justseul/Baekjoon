def solution(s):
    s = list(s)
    answer_list = []
    cnt = 0
    if(s[0] == ')') :
        return  False;
    
    for i in s:
        if i == '(':
            answer_list.append(i)
            cnt += 1
        if i == ')' and len(answer_list) > 0  :
            answer_list.pop()
            cnt -= 1
        

    if(len(answer_list)>1 or cnt != 0):
        answer = False    
    else:
        answer = True
    return answer