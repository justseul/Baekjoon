def solution(clothes):
    wardrobe = dict()
    for c, t in clothes:
        if t not in wardrobe.keys():
            wardrobe[t] = [c]
        else:
            wardrobe[t].append(c)
    sum = 1
    for i in wardrobe.values():
        sum *= len(i)+1
    return sum-1