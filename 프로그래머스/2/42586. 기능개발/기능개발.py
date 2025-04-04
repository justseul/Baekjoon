def solution(progresses, speeds):
    day_arr = [a // b if a % b == 0 else a // b + 1 
               for a, b in zip([100 - x for x in progresses], speeds)]

    answer = []
    current_day = day_arr[0]
    cnt = 1

    for day in day_arr[1:]:
        if day <= current_day:
            cnt += 1
        else:
            answer.append(cnt)
            current_day = day
            cnt = 1
    answer.append(cnt)
    return answer