import sys
from collections import deque

sys.stdin = open("input01.txt")

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]


def bfs(matrix, x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    matrix[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


cntlist = [bfs(matrix, i, j) for i in range(n) for j in range(n) if matrix[i][j] == 1]
cntlist.sort()
print(len(cntlist))
for i in range(len(cntlist)):
    print(cntlist[i])
