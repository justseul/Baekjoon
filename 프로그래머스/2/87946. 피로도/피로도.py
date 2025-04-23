import itertools
def solution(k, dungeons):
    max_d = 0
    for i in itertools.permutations(dungeons):
        k_temp = k
        cnt = 0
        for need, spend in i:
            if need <= k_temp:
                k_temp -= spend
                cnt += 1
        if cnt > max_d: max_d = cnt
    return max_d
