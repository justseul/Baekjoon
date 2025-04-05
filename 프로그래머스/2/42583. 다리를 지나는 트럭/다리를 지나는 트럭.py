def solution(bridge_length, weight, truck_weights):
    b = [0]*bridge_length
    time = 0
    b_w = 0
    while b_w != 0 or truck_weights:
        time += 1
        bye = b.pop(0)
        b_w -= bye
        if truck_weights:
            if (b_w + truck_weights[0] <= weight):
                now = truck_weights.pop(0)
                b.append(now)
                b_w += now
            else:
                b.append(0)
        else:
            b.append(0)
    return time