def solution(clothes):
    dic = {}
    m = 1

    for i, j in clothes:
        dic[j] = 0

    for i, j in clothes:
        if j in dic.keys():
            dic[j] += 1

    for i in dic.values():
        m *= i +1

    answer = m -1
    return answer