import sys

input = sys.stdin.readline

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

while True:
    # 1. 현재 칸이 청소되지 않았으면 청소
    if graph[r][c] == 0:
        graph[r][c] = 2  # 청소된 칸은 2로 표시
        cnt += 1

    cleaned = False
    for _ in range(4):
        # 2. 왼쪽 방향으로 회전
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        # 3. 앞쪽 칸이 청소되지 않은 경우 전진
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    # 4. 네 방향 모두 청소되어 있거나 벽인 경우 후진
    if not cleaned:
        back_dir = (d + 2) % 4
        r_back = r + dx[back_dir]
        c_back = c + dy[back_dir]

        # 후진할 수 있으면 후진
        if 0 <= r_back < n and 0 <= c_back < m and graph[r_back][c_back] != 1:
            r, c = r_back, c_back
        else:
            # 후진도 불가능 → 종료
            break

print(cnt)
