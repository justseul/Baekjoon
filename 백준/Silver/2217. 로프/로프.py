import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for i in range(n)]

rope.sort()
answer = 0
for i in range(len(rope)):
    if answer < (len(rope) - i) * rope[i]:
        answer = (len(rope) - i) * rope[i]
print(answer)