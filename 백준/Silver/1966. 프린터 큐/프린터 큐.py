import sys

n = int(sys.stdin.readline())

for i in range(n):
    num, idx = map(int, sys.stdin.readline().split())
    seq = list(map(int, sys.stdin.readline().split()))
    cnt = 0 
    
    while(1):
        if seq[0] == max(seq):
            seq.pop(0)
            idx -= 1
            cnt += 1
            if idx < 0: 
                print(cnt)
                break
        else: 
            seq.append(seq.pop(0))
            idx -= 1
            if idx < 0 :
                idx = len(seq) - 1