e, s, m = map(int,input().split())
e1, s1, m1 = 1, 1, 1
year = 1
while(1):
    
    if e == e1 and s == s1 and m == m1:
        print(year)
        break
    if e1 == 15:
        e1 = 0
    if s1 == 28:
        s1 = 0
    if m1 == 19:
        m1 = 0
    e1 += 1
    s1 += 1
    m1 += 1
    year += 1
    