n = int(input())
answer = []
for i in range(n):
    b = list(input())
    answer = []
    for j in range(len(b)):
        if b[j] == "(":
            answer.append("(") 
        elif len(answer) == 0 and b[j] == ")":
            print("NO")
            break
        elif b[j] == ")":
            answer.pop()
        # print(answer)

        if len(answer) == 0 and len(b) == j+1:
            print("YES")
        elif len(answer) != 0 and len(b) == j+1:
            print("NO")