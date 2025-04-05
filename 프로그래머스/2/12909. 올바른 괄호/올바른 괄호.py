def solution(s):
    answer = []
    for i in range(len(list(s))):
        if s[i] =='(':
            answer.append('(')
        elif len(answer) == 0 : 
            return False
        else: answer.pop()
    if answer : return False
    else: return True
        