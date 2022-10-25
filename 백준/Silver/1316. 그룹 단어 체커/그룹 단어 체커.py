N = int(input())
cnt = 0
for i in range(N):
    word = input()
    for i in range(len(list(word))):
        
        if word.find(word[i],i+1)-i > 1:        
            break
        if i == len(list(word))-1:
            cnt += 1   
print(cnt)