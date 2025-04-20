s = input().rstrip()
ans = 0
for _ in range(int(input())):
    ring = input()
    
    for i in range(len(ring)):
        ring = ring[1:] + ring[0]
        if ring.find(s) >= 0:
            ans += 1
            break
print(ans)