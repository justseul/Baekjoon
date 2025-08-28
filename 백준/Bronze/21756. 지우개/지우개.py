import sys
input = sys.stdin.readline

n = int(input())
answer = [ i for i in range(1, n+1)]

while len(answer) != 1:
    temp = []
    for i in range(len(answer)):
        if i % 2 == 1:
            temp.append(answer[i])
    answer = temp

print(answer[0])