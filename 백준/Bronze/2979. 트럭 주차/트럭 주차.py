import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
array = [0]*101

for i in range(3):
    x, y = map(int, input().split())
    for j in range(x, y):
        array[j] += 1

for idx in range(len(array)):
    if array[idx] == 1:
        array[idx] *= a
    elif array[idx] == 2:
        array[idx] *= b
    elif array[idx] == 3:
        array[idx] *= c
print(sum(array))
