def solution(priorities, location):
    idx_list = list(range(len(priorities)))
    cnt = 0
    while(1):
        if priorities[0] == max(priorities) and idx_list[0] == location:
            cnt += 1
            return cnt
        elif priorities[0] == max(priorities):
            priorities.pop(0)
            idx_list.pop(0)
            cnt += 1
        else:
            priorities.append(priorities.pop(0))
            idx_list.append(idx_list.pop(0))
        print(priorities)
        print(idx_list)
        print(cnt)
    