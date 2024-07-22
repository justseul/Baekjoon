loc = input()

alphabet = {}

for i in range(97, 105):
    alphabet[chr(i)] = i-96

x, y = int(alphabet[loc[0]]), int(loc[1])

knight = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

cnt = 0

for i, j in knight:
    nx = x + i
    ny = y + j
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1
        print(nx,ny)

print(cnt)

