n, k = map(int, input().split())


l = list(i for i in range(1,n+1))

answer = [] 
index = 0

for i in range(n):
    index += k-1
    if index >= len(l):
        index %= len(l)
    answer.append(str(l.pop(index
                           )))
print("<",", ".join(answer)[:],">", sep='')