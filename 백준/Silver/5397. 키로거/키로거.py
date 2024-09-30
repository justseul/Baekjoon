from collections import deque
import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    pw = sys.stdin.readline().strip()
    r_p = deque()
    l_p = deque()

    for i in pw:
        if i == '<':
            if l_p:
                r_p.appendleft(l_p.pop())
        elif i == '>':
            if r_p :
                l_p.append(r_p.popleft())
        elif i == '-' :
            if l_p :
                l_p.pop()
        else:
            l_p.append(i)

    answer = "".join(l_p+r_p)
    print(answer)