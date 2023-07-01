import sys

text = list(sys.stdin.readline().rstrip())
a = []
n = int(sys.stdin.readline().rstrip())


for _ in range(n):
    c = list(sys.stdin.readline().rstrip())
    if c[0] == "L" and text :
        a.append(text.pop())
    elif c[0] == "D" and a:
        text.append(a.pop())
    elif c[0] == "B" and text :
        text.pop()
    elif c[0] == "P":
        text.append(c[2])

        

print("".join(text + list(reversed(a))))