def solution(priorities, location):
    index = []
    i = 0
    for idx in range(len(priorities)):
        index.append(idx)

    while(priorities != sorted(priorities, reverse=True)):
        if priorities[i] < max(priorities[i:]):
            # print('{0} 실행'.format(i),priorities[i])
            priorities.append(priorities[i])
            priorities.pop(i)        
            index.append(index[i])
            index.pop(i)
        else:
            i += 1

    return index.index(location)+1