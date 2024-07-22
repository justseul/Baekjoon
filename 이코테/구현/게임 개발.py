map_x, map_y = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(map_x)]

d_state = [(0,-1),(-1,0),(0,1),(1,0)]
cnt = 0
while(1):
    if map[x][y] == 0: 
        cnt += 1
        s_cnt = 0
        map[x][y] = 1
    nx = x + d_state[d][0]
    ny = y + d_state[d][1]
    if map[nx][ny] == 0: 
        x, y = nx ,ny
    if d == 0: d += 3
    else: d -= 1
    s_cnt += 1
    if s_cnt >= 4: break

print(cnt)