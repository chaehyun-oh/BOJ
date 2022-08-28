from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 소수찾기 1978

# n = int(input())
# cnt = 0
# nums = list(map(int, input().split()))

# for n in nums:
#     err = 0
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 err += 1
#         if err == 0:
#             cnt += 1
# print(cnt)

# 섬의 개수 4963

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0,  -1, -1, -1, 0, 1]


def bfs(i, j):
    matrix[i][j] = 0
    q = [[i, j]]
    while q:
        a, b = q[0][0], q[0][1]
        q.pop(0)
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and matrix[x][y] == 1:
                matrix[x][y] = 0
                q.append([x, y])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split()))for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)


# ----
