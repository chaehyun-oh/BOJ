import sys

sys.stdin = open("input01.txt")

# 1926 그림

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

area = []
cnt = 0


def bfs(x, y):
    w = 1
    q = [(x, y)]
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1 and not chk[nx][ny]:
                    w += 1
                    chk[nx][ny] = 1
                    q.append((nx, ny))
    return w


cnt, wide = 0, 0

chk = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not chk[i][j]:
            cnt += 1
            chk[i][j] = 1
            wide = max(wide, bfs(i, j))

print(cnt)
print(wide)
