def solution(array, commands):
    answer = list()
    for first, last, n in commands:
        sort_array = sorted(array[first-1:last])
        answer.append(sort_array[n-1])
    return answer