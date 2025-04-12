def solution(name):
    move = len(name) - 1
    answer = 0
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), 26 - (ord(char) - ord('A')))
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        distance = min(
            move,
            i * 2 + len(name) - next_idx,
            (len(name) - next_idx) * 2 + i
        )
        move = min(move, distance)
    return answer + move
