import sys
input = sys.stdin.readline
s = input().rstrip("\n")   
space_left = int(input())      
cnt = list(map(int, input().split()))  

title_chars = []
prev = None
ok = True

for ch in s:
    if ch == prev:
        continue

    if ch == ' ':
        space_left -= 1
        if space_left < 0:
            ok = False
            break
    else:
        idx = ord(ch.lower()) - 97
        cnt[idx] -= 1
        if cnt[idx] < 0:
            ok = False
            break

        if prev == ' ' or prev is None:
            title_chars.append(ch.upper())
    prev = ch

if not ok:
    print(-1)
    sys.exit(0)

title = ''.join(title_chars)
prev = None
for ch in title:
    if ch == prev:
        continue
    idx = ord(ch.lower()) - 97
    cnt[idx] -= 1
    if cnt[idx] < 0:
        print(-1)
        sys.exit(0)
    prev = ch

print(title)
