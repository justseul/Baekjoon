import sys
input = sys.stdin.readline
 
n = int(input())
point = []
acc = [0] * (n+1)  
for i in range(n):
    point.append(int(input()))
    acc[i+1] = acc[i] + point[i]
 
total = acc[n]    

ans = 0
for i in range(1, n+1):
    start, end = i, n
    while start <= end:
        mid = (start+end) // 2
        length1 = acc[mid] - acc[i-1]
        length2 = total - length1
        if length1 < length2:
            start = mid + 1
        else:
            end = mid - 1
        ans = max(ans, min(length1, length2))
print(ans)