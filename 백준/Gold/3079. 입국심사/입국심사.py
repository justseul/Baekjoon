import sys

n, m = map(int, input().split())
employee = [int(input())for _ in range(n)]

lowTime = 0
highTime = max(employee) * m

while(lowTime <= highTime):
    mid = (lowTime + highTime) // 2
    total = 0
    for i in employee:
        total += mid//i
    if total >= m:
        highTime = mid - 1
        answer = mid
    else:
        lowTime = mid + 1

print(answer)