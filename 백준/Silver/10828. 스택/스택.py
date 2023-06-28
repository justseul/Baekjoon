import sys
n = int(input())
stack = []
for i in range(n):
    a =  sys.stdin.readline().split()
    if a[0]=='push':
        stack.append(a[1])
    elif a[0]=='pop' and len(stack)==0:
        print(-1)
    elif a[0]=='pop':
        print(int(stack.pop()))
    elif a[0]=='size':
        print(len(stack))
    elif a[0]=='empty' and len(stack) == 0:
        print(1)
    elif a[0]=='empty':
        print(0)
    elif a[0]=='top' and len(stack)==0:
        print(-1)
    elif a[0]=='top':
        print(int(stack[-1]))