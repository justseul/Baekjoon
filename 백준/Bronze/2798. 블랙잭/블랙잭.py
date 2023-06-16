n, m = map(int,input().split())
card = list(map(int,input().split()))

l = []
for i in range(len(card)-2):
    for j in range(i+1,len(card)-1):
        for z in range(j+1, len(card)):
            if card[i]+card[j]+card[z] > m:
                continue
            else:
                l.append(card[i]+card[j]+card[z])
print(max(l))