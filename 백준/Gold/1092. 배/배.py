import sys
input = sys.stdin.readline

n = int(input())
limit = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
day = 0

limit.sort(reverse=1)
box.sort(reverse=1)

if box[0] > limit[0]:
    print(-1)
else:
    while box:
        for i in range(n):
            for j in range(len(box)):
                if limit[i] >= box[j]:
                    box.pop(j)
                    break
        day += 1

    print(day)