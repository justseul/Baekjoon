l1 = []
l2 = []
for _ in range(3):
  a, b =map(int,input().split())
  if a in l1:
    l1.remove(a)
  else:
    l1.append(a)
  if b in l2:
    l2.remove(b)
  else:
    l2.append(b)

print(f"{l1[0]} {l2[0]}")

