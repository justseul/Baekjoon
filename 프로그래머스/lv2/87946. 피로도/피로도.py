from itertools import permutations

def solution(k, dungeons):
    sample = list(permutations(dungeons, len(dungeons)))
    sample_cnt = []

    for i in range(len(sample)):
        cnt = 0
        k_1 = k
        for j in range(len(dungeons)):
            if(k_1 < sample[i][j][0] ):
                pass
            else:
                k_1 -= sample[i][j][1]
                cnt += 1


        sample_cnt.append(cnt)

    
    return max(sample_cnt)