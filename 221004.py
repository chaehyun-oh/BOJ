import sys

sys.setrecursionlimit(100000)
sys.stdin = open("input01.txt")


# 2468 안전 영역
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and matrix[nx][ny] > h:
            visit[nx][ny] = True
            dfs(nx, ny, h)


n = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 1
for m in range(max(map(max, matrix))):
    visit = [[False] * n for _ in range(n)]
    sz = 0
    for j in range(n):
        for k in range(n):
            if matrix[j][k] > m and not visit[j][k]:
                sz += 1
                visit[j][k] = True
                dfs(j, k, m)
    ans = max(ans, sz)

print(ans)
