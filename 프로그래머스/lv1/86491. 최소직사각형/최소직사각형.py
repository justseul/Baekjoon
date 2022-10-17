def solution(sizes):
    max_l = []
    min_l = []
    for x, y in sizes:
        max_l.append(max(x,y))
        min_l.append(min(x,y))
    answer = max(max_l) * max(min_l)
    return answer