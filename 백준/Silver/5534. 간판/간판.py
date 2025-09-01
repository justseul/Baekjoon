import sys
input = sys.stdin.readline

N = int(input().strip())
name = input().strip()
m = len(name)

ans = 0
for _ in range(N):
    s = input().strip()
    L = len(s)
    ok = False

    for i in range(L):
        if s[i] != name[0]:
            continue
        for j in range(i, L):
            if s[j] != name[-1]:
                continue
            if m == 1:  
                ok = True
                break
            span = j - i
            if span % (m - 1) != 0:
                continue
            d = span // (m - 1)
            if d == 0:
                continue

            good = True
            for k in range(m):
                idx = i + k * d
                if idx < 0 or idx >= L or s[idx] != name[k]:
                    good = False
                    break
            if good:
                ok = True
                break
        if ok:
            break

    if ok:
        ans += 1

print(ans)
