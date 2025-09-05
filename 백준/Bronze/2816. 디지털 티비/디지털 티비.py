import sys
input = sys.stdin.readline

n = int(input().strip())
ch = [input().strip() for _ in range(n)]

ops = []

idx1 = ch.index("KBS1")
ops.append('1' * idx1)            
for _ in range(idx1):             
    i = ch.index("KBS1")
    ch[i-1], ch[i] = ch[i], ch[i-1]
    ops.append('4')

idx2 = ch.index("KBS2")
ops.append('1' * idx2)            
while ch.index("KBS2") > 1:
    i = ch.index("KBS2")
    ch[i-1], ch[i] = ch[i], ch[i-1]
    ops.append('4')

print(''.join(ops))
