def solution(sizes):
    big = list()
    small = list()
    for i in sizes:
        big.append(max(i))
        small.append(min(i))
    return max(big) * max(small)
            