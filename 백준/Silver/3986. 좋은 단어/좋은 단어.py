import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    s = input().strip()        
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    if not stack:             
        cnt += 1

print(cnt)
